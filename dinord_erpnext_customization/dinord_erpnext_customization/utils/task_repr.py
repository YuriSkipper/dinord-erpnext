import frappe


class TaskBase:
    def __init__(self, instance):
        self.name = instance.get('name')
        self.subject = instance.get('subject')
        self.creation = instance.get('creation')
        self.item_type = instance.get('type')
        self.begin = instance.get('exp_start_date')
        self.end = instance.get('exp_end_date')
        self.parent = instance.get("parent_task")
        self.order_id = instance.get('idx')

    def to_dict(self):
        result = {
            'id': self.name,
            'subject': self.subject,
            'date': self.creation,
            'parentId': self.parent,
            'state': self.item_type,
            'beginDate': self.begin,
            'endDate': self.end,
            'orderId': self.order_id
        }
        return result


class TaskRepr(TaskBase):

    def __init__(self, task):
        super().__init__(task)
        self.children = self.__get_children()

    
    def __get_children(self):
        result = []
        children = frappe.db.get_all(
            'Task',
            filters={
                'parent_task': self.name
            },
            fields='*'
        )
        for child in children:
            task = TaskBase(child)
            result.append(task.to_dict())
        return result

    def to_dict(self):
        result = super().to_dict()
        result['children'] = self.children
        return result
