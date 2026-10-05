# Machine Learning & Buyer Barometer

The pricing engine uses a **Multiple Linear Regression** formulation to estimate property market prices from key physical and location attributes.

---

## 🧮 Mathematical Formulation

The predicted price $\hat{y}$ is computed as:

$$\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n + \epsilon$$

Where:
- $\beta_0$: Base intercept
- $x_1, \dots, x_n$: One-hot encoded feature vector containing:
  - `area_sqft`
  - `bedrooms`
  - `bathrooms`
  - `property_age`
  - `has_parking`
  - Categorical types: Apartment, Villa, Residential, Commercial, Entertainment
  - City tiers: Patiala, Chandigarh, Mohali, Delhi NCR, Bangalore, Mumbai
  - Furnishing tiers: Unfurnished, Semi-Furnished, Fully-Furnished

---

## 📏 Evaluation Metrics

Model performance is evaluated using:

### Mean Squared Error (MSE)
$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

### Root Mean Squared Error (RMSE)
$$RMSE = \sqrt{MSE}$$

### Coefficient of Determination ($R^2$)
$$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$$

---

## 🧭 The Buyer Barometer

The **Buyer Barometer** compares the seller's asking price against the ML estimated price:

$$\text{Variance \%} = \frac{\text{Asking Price} - \hat{y}}{\hat{y}} \times 100$$

### Rating Bands:
1. **🌟 Great Deal:** Variance $\le -10\%$ (property listed at a bargain below market baseline).
2. **⚖️ Fair Market Price:** $-10\% < \text{Variance} < 10\%$ (aligned with current market trends).
3. **💎 Premium Listing:** Variance $\ge 10\%$ (seller is asking for a premium above typical neighborhood comparable assets).
