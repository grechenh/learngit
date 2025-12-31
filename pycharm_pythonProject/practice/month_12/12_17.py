class Employee:
    def __init__(self, employee_id: str, name: str, department: str, monthly_salary: int):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.monthly_salary = monthly_salary

    def __str__(self):
        """员工 1: E001, 张三, 技术部, 15000"""
        return f"员工ID：{self.employee_id}    姓名：{self.name}    部门：{self.department}    月薪：{self.monthly_salary}"


class EmployeeManager:
    def __init__(self):
        self.list_cont = []
        self.dict_cont = {}

    def add_employee(self, employee_id, name, department, monthly_salary):
        """添加类对象"""
        employee = Employee(employee_id=employee_id, name=name, department=department, monthly_salary=monthly_salary)
        self.list_cont.append(employee)
        if department not in self.dict_cont:
            self.dict_cont[department] = []
        self.dict_cont[department].append(employee)

    def quick_order(self, arr: list):
        """定义快速排序"""
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        # 分区操作(降序)
        left = [x for x in arr[1:] if x.monthly_salary >= pivot.monthly_salary]  # 大于等于基准的元素
        right = [x for x in arr[1:] if x.monthly_salary < pivot.monthly_salary]  # 小于基准的元素

        # 递归排序并合并
        return self.quick_order(left) + [pivot] + self.quick_order(right)
        pass

    def order_employee(self):
        """实现快速排序算法进行薪资排序"""
        if not self.list_cont:
            return []
        ordered_list = self.quick_order(self.list_cont)
        return ordered_list

    def show(self, department: str):
        """"按部门显示"""
        if department not in self.dict_cont:
            return []
        items = self.dict_cont[department]
        return items


def main():
    item = EmployeeManager()
    '''添加示例'''
    """
        员工 1: E001, 张三, 技术部, 15000
        员工 2: E002, 李四, 市场部, 12000
        员工 3: E003, 王五, 技术部, 18000
        员工 4: E004, 赵六, 市场部, 10000
    """
    employees = [
        ("E001", "张三", "技术部", 15000),
        ("E002", "李四", "市场部", 12000),
        ("E003", "王五", "技术部", 18000),
        ("E004", "赵六", "市场部", 10000)
    ]
    for employee_id, name, department, monthly_salary in employees:
        item.add_employee(employee_id=employee_id, name=name, department=department, monthly_salary=monthly_salary)
        print(f"添加员工: {name} (ID: {employee_id})     部门：{department}     月薪: {monthly_salary}")

    ordered_employee = item.order_employee()
    print("排序后：")
    for order_item in ordered_employee:
        print(order_item)

    get_department = "市场部"
    show_employee = item.show(get_department)
    print(f"按照{get_department}查询：")
    for show_item in show_employee:
        print(show_item)


if __name__ == '__main__':
    main()
