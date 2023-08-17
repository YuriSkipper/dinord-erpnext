from erpnext.projects.doctype.task.utils import TaskRepr
import frappe

from ..utils.task_repr import TaskRepr

@frappe.whitelist(methods=['GET', 'POST'])
def get_task(data=None):
    
    result = []
    db_result = frappe.db.get_all("Task", fields="*", order_by="name asc")
    for item in db_result:
        task = TaskRepr(item)
        task_dict = task.to_dict()
        result.append(task_dict)
    return result