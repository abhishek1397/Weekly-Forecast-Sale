## 📊 Walmart Sales Prediction Datasets

This project uses a structured dataset provided for Walmart weekly sales forecasting, consisting of **four core CSV files**:

---

### 📁 1. `train.csv`

Contains the historical weekly sales data for Walmart stores and departments.

| Column Name     | Description                                    |
|------------------|------------------------------------------------|
| `Store`         | Unique identifier for each store               |
| `Dept`          | Unique identifier for each department          |
| `Date`          | Week of the sale (YYYY-MM-DD)                  |
| `Weekly_Sales`  | Weekly sales amount                            |
| `IsHoliday`     | Boolean flag: `True` if the week includes a holiday |

📌 **Note**: This is the primary dataset used to train the model.

---

### 📁 2. `test.csv`

Contains the structure of future weeks for which we need to predict sales (i.e., target variable `Weekly_Sales` is not included).

| Column Name | Description                            |
|--------------|----------------------------------------|
| `Store`     | Store identifier                       |
| `Dept`      | Department identifier                  |
| `Date`      | Target week                            |
| `IsHoliday` | Indicates whether the week has a holiday |

📌 **Purpose**: Used during prediction and evaluation.

---

### 📁 3. `stores.csv`

Provides meta-information about each Walmart store.

| Column Name | Description                        |
|--------------|------------------------------------|
| `Store`     | Store identifier                   |
| `Type`      | Type of the store (A, B, or C)     |
| `Size`      | Store size in square feet          |

📌 **Usage**: Useful for feature engineering (e.g., analyzing impact of size/type on sales).

---

### 📁 4. `features.csv`

Includes additional weekly-level features such as marketing, economy, and holiday flags.

| Column Name      | Description                                           |
|-------------------|-------------------------------------------------------|
| `Store`          | Store identifier                                      |
| `Date`           | Week of observation                                   |
| `Temperature`    | Average temperature for the week                      |
| `Fuel_Price`     | Cost of fuel                                          |
| `CPI`            | Consumer Price Index                                  |
| `Unemployment`   | Unemployment rate                                     |
| `MarkDown1-5`    | Promotional markdowns across 5 different campaigns    |
| `IsHoliday`      | Indicates if that week included a major holiday       |

📌 **Usage**: These features can improve forecasting performance significantly when engineered properly.

---

