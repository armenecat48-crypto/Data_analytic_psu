import pandas as pd


DATA_PATH = "day02/case02_marketing/data/marketing_performance.csv"

df = pd.read_csv(DATA_PATH)

budget_analysis = df[
	["Channel", "Spend", "Revenue", "Conversions"]
].copy()

budget_analysis["Spend_Band"] = pd.qcut(
	budget_analysis["Spend"],
	q=4,
	labels=["Low", "Medium", "High", "Very High"]
)

budget_summary = (
	budget_analysis
	.groupby(["Channel", "Spend_Band"], observed=True)
	.agg(
		Spend=("Spend", "sum"),
		Revenue=("Revenue", "sum"),
		Conversions=("Conversions", "sum"),
		Campaign_Rows=("Channel", "count")
	)
	.reset_index()
)

budget_summary["ROAS_calc"] = (
	budget_summary["Revenue"] / budget_summary["Spend"]
)

print(budget_summary.sort_values(["Channel", "Spend_Band"]))

