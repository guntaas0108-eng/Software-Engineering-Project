# Course Evaluation Metrics (UCS503P)

The platform evaluates the success of the engineering workflow based on measurable, attributable metrics.

---

## 🎯 1. Primary Evaluation Metric: Time-to-Appointment

### Definition
The duration measured between a prospective buyer's initial message regarding a listing and the seller's confirmed site visit appointment.

### Course Objective
$$\text{Median Time-to-Appointment} \le 2.0 \text{ hours}$$

### Technical Attribution
- **Inquiry Timestamp:** Captured in the `messages` / `appointments` table at first contact ($t_0$).
- **Confirmation Timestamp:** Captured when seller confirms the visit slot via API ($t_1$).
- **Elapsed Duration:** $\Delta t = t_1 - t_0$.
- **Aggregated Statistic:** Calculated via median query on confirmed appointments in `/api/metrics`.

---

## 📈 2. Secondary Metrics

1. **Prediction Accuracy:**
   - Evaluated by holding regression MSE within 10% bounds of actual representative market pricing.
2. **Engagement Rate:**
   - Percentage of total properties with active negotiation threads:
     $$\text{Engagement Rate} = \frac{\text{Engaged Properties}}{\text{Total Properties}} \times 100$$
3. **Availability / Pilot Reliability:**
   - Web application uptime $\ge 99\%$ throughout review and pilot demonstration.
