# Week 10 Journal — Sprint 5: Buyer Barometer & Responsive Regression

## Student
Dhruv Rajput — Person 3: Frontend, Buyer & Buyer Barometer

## Objective
Take additional responsibility for buyer experience regression testing while completing the buyer-facing payment and property information screens.

## Work Done
- Reviewed Buyer Barometer states for Great Deal, Fair Price, Above Market and Pending Analysis.
- Checked that the displayed comparison uses the property's listed price and available predicted price rather than a hardcoded frontend value.
- Reviewed responsive layouts for property cards, property details, saved properties, checkout and payment result screens.
- Prepared UI checks for long locality names, missing property images, unavailable predicted valuations and empty search results.
- Coordinated with Haneesh to keep the ML valuation explanation consistent with the model's actual output and documented limitations.
- Coordinated with Guntaas to verify that buyer pages consume the correct property, appointment and payment records.

## Outcome
The buyer-facing regression checklist covers the main discovery, valuation and payment states. Visual and functional acceptance still requires browser testing against the running application.

## Issues / Follow-up
- Test the buyer flow at desktop and mobile viewport sizes.
- Confirm that missing ML predictions display a pending/unavailable state rather than a fabricated price.
- Check search and filter combinations, saved-property actions and navigation back to property details.
- Verify that payment result screens refresh from backend status.
- Record screenshots or test evidence only after the actual browser checks are performed.

## Learning
I learned that frontend quality depends on correct data states as much as visual layout. A clear unavailable state is better than displaying a misleading value.
