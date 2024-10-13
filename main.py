# Phần 1: Triển khai hàm NextDate

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def next_date(year, month, day):
    if not (1850 <= year <= 2050):
        return "Error: Year out of range"
    if not (1 <= month <= 12):
        return "Error: Month out of range"
    if not (1 <= day <= 31):
        return "Error: Day out of range"

    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_leap_year(year):
        days_in_month[2] = 29

    if day > days_in_month[month]:
        return f"Error: Invalid date {year}-{month}-{day}"

    if day < days_in_month[month]:
        return f"{year}-{month:02d}-{day+1:02d}"
    else:
        if month < 12:
            return f"{year}-{month+1:02d}-01"
        else:
            return f"{year+1}-01-01"

# Phần 2: Thiết kế các trường hợp kiểm thử

# 2.1 Phân vùng tương đương
eq_classes = [
    # Tháng 30 ngày (M30)
    (2023, 4, 15, "2023-04-16"),  # Ngày bình thường
    (2023, 4, 30, "2023-05-01"),  # Ngày cuối tháng
    
    # Tháng 31 ngày (M31)
    (2023, 1, 15, "2023-01-16"),  # Ngày bình thường
    (2023, 1, 31, "2023-02-01"),  # Ngày cuối tháng
    
    # Tháng 2 (February)
    (2023, 2, 15, "2023-02-16"),  # Ngày bình thường, năm không nhuận
    (2023, 2, 28, "2023-03-01"),  # Ngày cuối tháng, năm không nhuận
    (2024, 2, 28, "2024-02-29"),  # Ngày 28/2, năm nhuận
    (2024, 2, 29, "2024-03-01"),  # Ngày cuối tháng, năm nhuận
    
    # Năm nhuận và không nhuận
    (2023, 12, 31, "2024-01-01"),  # Chuyển sang năm nhuận
    (2024, 12, 31, "2025-01-01"),  # Chuyển từ năm nhuận sang năm thường
]

# 2.2 Phân tích giá trị biên
boundary_cases = [
    (1850, 1, 1, "1850-01-02"),   # Năm nhỏ nhất hợp lệ
    (2050, 12, 31, "Error: Invalid date 2050-12-31"),  # Năm lớn nhất hợp lệ
    (1849, 12, 31, "Error: Year out of range"),  # Năm dưới giới hạn
    (2051, 1, 1, "Error: Year out of range"),    # Năm trên giới hạn
    (2023, 0, 1, "Error: Month out of range"),   # Tháng dưới giới hạn
    (2023, 13, 1, "Error: Month out of range"),  # Tháng trên giới hạn
    (2023, 1, 0, "Error: Day out of range"),     # Ngày dưới giới hạn
    (2023, 1, 32, "Error: Invalid date 2023-1-32"),  # Ngày trên giới hạn
]

# 2.3 Bảng quyết định
decision_table = [
    # Rule 1: Ngày bình thường
    (2023, 5, 15, "2023-05-16"),
    # Rule 2: Ngày cuối tháng 30 ngày
    (2023, 4, 30, "2023-05-01"),
    # Rule 3: Ngày cuối tháng 31 ngày
    (2023, 3, 31, "2023-04-01"),
    # Rule 4: Ngày cuối năm
    (2023, 12, 31, "2024-01-01"),
    # Rule 5: 28/2 năm không nhuận
    (2023, 2, 28, "2023-03-01"),
    # Rule 6: 29/2 năm nhuận
    (2024, 2, 29, "2024-03-01"),
    # Rule 7: Ngày không hợp lệ
    (2023, 2, 30, "Error: Invalid date 2023-2-30"),
]

# Phần 3: Chạy kiểm thử

def run_tests(test_cases, test_name):
    print(f"\nRunning {test_name}:")
    for case in test_cases:
        year, month, day, expected = case
        result = next_date(year, month, day)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: {year}-{month:02d}-{day:02d}, Expected: {expected}, Got: {result}, Status: {status}")

run_tests(eq_classes, "Equivalence Class Tests")
run_tests(boundary_cases, "Boundary Value Tests")
run_tests(decision_table, "Decision Table Tests")