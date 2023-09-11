def get_input(prompt):
    return input(prompt).strip()

def main():
    hourly_rate = get_input("Enter your hourly wage (leave blank if unknown): ")

    if not hourly_rate:
        weekly_rate = get_input("Enter your weekly wage (leave blank if unknown): ")
        if not weekly_rate:
            monthly_rate = get_input("Enter your monthly wage: ")
            if not monthly_rate:
                print("Error: No wage data entered.")
                return
            calculation_base = "month"
            average_work_hours_week = float(get_input("Enter average hours you work per week: "))
            work_days_month = (average_work_hours_week / 7) * 30  # Assuming 30 days in a month for simplicity
            work_time = work_days_month
            rate = float(monthly_rate) / work_time
        else:
            calculation_base = "week"
            average_work_hours_week = float(get_input("Enter average hours you work per week: "))
            work_time = average_work_hours_week
            rate = float(weekly_rate) / work_time
    else:
        calculation_base = "hour"
        work_time = 1
        rate = float(hourly_rate)

    product_price = float(get_input("Enter the price of the product you want to buy: "))

    work_units_needed = product_price / rate

    if calculation_base == "hour":
        hours_needed = work_units_needed
        minutes_needed = (hours_needed % 1) * 60
    elif calculation_base == "week":
        weeks_needed = work_units_needed
        hours_needed = (weeks_needed % 1) * average_work_hours_week
        minutes_needed = (hours_needed % 1) * 60
    else:  # month
        months_needed = work_units_needed
        weeks_needed = (months_needed % 1) * 4  # Assuming 4 weeks in a month for simplicity
        hours_needed = (weeks_needed % 1) * average_work_hours_week
        minutes_needed = (hours_needed % 1) * 60

    print(f"\nIt will cost you {int(hours_needed)} hours and {int(minutes_needed)} minutes of work to afford this product.")

if __name__ == "__main__":
    main()
