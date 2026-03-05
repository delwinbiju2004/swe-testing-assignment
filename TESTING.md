# Testing Strategy

This project uses a combination of unit testing and integration testing to ensure the reliability of the Quick-Calc application.

## Testing Pyramid

The testing pyramid suggests having many unit tests and fewer integration tests. This project follows that idea:

- 8 Unit Tests
- 2 Integration Tests

Unit tests verify individual calculator functions, while integration tests verify how components work together.

## Black-box vs White-box Testing

Unit tests mainly use **white-box testing**, because we directly test internal functions like add(), subtract(), multiply(), and divide().

Integration tests use **black-box testing**, because we test the system behaviour without focusing on internal implementation.

## Functional vs Non-Functional Testing

This project focuses on **functional testing**, ensuring that calculator operations produce correct results.

Non-functional aspects such as performance or security were not tested because they are outside the scope of this assignment.

## Regression Testing

The test suite helps detect regressions. If future changes introduce bugs, running the tests will immediately reveal if existing functionality has broken.

## Test Results

| Test Name | Type | Status |
|-----------|------|--------|
| Addition Test | Unit | Pass |
| Subtraction Test | Unit | Pass |
| Multiplication Test | Unit | Pass |
| Division Test | Unit | Pass |
| Divide by Zero Test | Unit | Pass |
| Negative Numbers Test | Unit | Pass |
| Decimal Numbers Test | Unit | Pass |
| Large Numbers Test | Unit | Pass |
| Full Calculation Test | Integration | Pass |
| Clear Function Test | Integration | Pass |

