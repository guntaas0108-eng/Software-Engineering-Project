"""
Model loader for PropertyPulse ML Price Predictor.
Plugs into Hugging Face Hub (Haneesh112/propertypulse-price-predictor)
with seamless local caching and resilient fallback.
"""
from functools import lru_cache
import logging
import os
from pathlib import Path

import joblib
from django.conf import settings
from huggingface_hub import hf_hub_download
from huggingface_hub.errors import HfHubHTTPError, GatedRepoError

logger = logging.getLogger(__name__)


def _get_local_model_path() -> Path:
    base_dir = getattr(settings, "BASE_DIR", Path(__file__).resolve().parent.parent)
    return Path(base_dir) / "ml_predictor" / "model.joblib"


@lru_cache(maxsize=1)
def load_model():
    """
    Downloads (once) and returns the trained model bundle:
        {"model": <sklearn LinearRegression>, "encoders": {...}, "feature_order": [...]}
    First attempts Hugging Face Hub download. If unauthorized (gated repo) or offline,
    resiliently falls back to local cached model.joblib.
    """
    repo_id = getattr(settings, "HF_MODEL_REPO_ID", "")
    filename = getattr(settings, "HF_MODEL_FILENAME", "model.joblib")
    token = getattr(settings, "HF_TOKEN", "") or None
    local_fallback = _get_local_model_path()

    # 1. Try Hugging Face Hub if repo_id is configured
    if repo_id:
        try:
            logger.info("Attempting to load model '%s' from Hugging Face Hub repo '%s'...", filename, repo_id)
            hf_path = hf_hub_download(repo_id=repo_id, filename=filename, token=token)
            logger.info("Successfully fetched model from Hugging Face Hub: %s", hf_path)
            return joblib.load(hf_path)
        except (GatedRepoError, HfHubHTTPError, Exception) as err:
            logger.warning(
                "Could not pull '%s' from Hugging Face Hub repo '%s' (%s). "
                "Checking for local fallback model at %s...",
                filename, repo_id, err, local_fallback
            )

    # 2. Local fallback model
    if local_fallback.exists():
        logger.info("Loading local model from %s", local_fallback)
        return joblib.load(local_fallback)

    # 3. If neither HF nor local file exists, generate and train on the fly
    logger.info("Local model not found. Generating and training baseline model bundle...")
    from .train.generate_dataset_and_train import generate_data, train_and_save
    df = generate_data()
    train_and_save(df)
    if local_fallback.exists():
        return joblib.load(local_fallback)

    raise RuntimeError(
        f"Unable to load model from Hugging Face Hub ('{repo_id}') or local path ('{local_fallback}')."
    )


def reload_model():
    """Call this after pushing an updated model to pick it up without restarting."""
    load_model.cache_clear()
    return load_model()
