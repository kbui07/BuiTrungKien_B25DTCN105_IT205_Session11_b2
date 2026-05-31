# 1. Dictionary employee gồm những key nào? employee_id, full_name, department, status
# 2. Vì sao dòng sau gây lỗi? Vì dictionary truy cập dữ liệu bằng key, không phải bằng index.
# 3. Dictionary có truy cập phần tử bằng index giống list không? không

employee = {"employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

employee_id = employee["employee_id"]
full_name = employee["full_name"]

employee["status"] = "official"

employee["base_salary"] = 15000000

del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)