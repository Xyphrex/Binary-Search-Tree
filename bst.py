'''
Your task is to complete the following functions which are marked by the TODO comment.
You are free to add properties and functions to the class as long as the given signatures remain identical.
Note: Please do not modify any existing function signatures, as it will impact your test results
'''


class Student:
    """Represents a node of a binary tree."""
    """These are the defined properties as described above, feel free to add more if you wish!"""
    """However do not modify nor delete the current properties."""
    def __init__(self, student_id, name, GPA) -> None:
        self.left = None
        self.right = None
        self.parent = None
        self.student_id = student_id
        self.name = name
        self.GPA = GPA

class BSTree:
    """
    Implements an unbalanced Binary Search Tree.
    """
    def __init__(self, *args) -> None:
        self.Root = None
        # Initialize the tree with a sequence if provided, don't modify the init
        if len(args) == 1:
            if isinstance(args[0], collections.Iterable):
                for x in args[0]:
                    self.insert(x[0], x[1])
            else:
                raise TypeError(str(args[0]) + " is not iterable")

    """-------------------------------PLEASE DO NOT MODIFY THE ABOVE (except you could add more properties in Student class) -------------------------------"""
    def insert(self, student_id, name, GPA) -> None:
        """
        Inserts a new Student into the tree.
        """
        """
        Utilized iterative approach instead of recursive one
        to reduce large memory overheads which may possibly occur
        in large trees
        """
        student_node = Student(student_id, name, GPA)

        if self.Root == None:
            self.Root = student_node
        else:
            current_root = self.Root
            while True:
                if current_root.student_id == student_id:
                    break
                elif current_root.student_id < student_id:
                    if current_root.right == None:
                        current_root.right = student_node
                        current_root.right.parent = current_root
                        break
                    else:
                        current_root = current_root.right

                elif current_root.student_id > student_id:
                    if current_root.left == None:
                        current_root.left = student_node
                        current_root.left.parent = current_root
                        break
                    else:
                        current_root = current_root.left


    def search(self, student_id) -> Student:
        """
        Searches for a student by student_id.
        """
        """
        Utilized iterative approach instead of recursive one
        to reduce large memory overheads which may possibly occur
        in large trees
        """
        if self.Root == None:
            return
        if self.Root.student_id == student_id:
            return self.Root
        else:
            current_root = self.Root
            while current_root != None:
                if current_root.student_id == student_id:
                    return current_root
                elif current_root.student_id < student_id:
                    current_root = current_root.right

                elif current_root.student_id > student_id:
                    current_root = current_root.left


    def delete(self, student_id) -> None:
        """
        Deletes a student from the tree by student_id.
        """
        student_node = self.search(student_id)
        if student_node == None:
            return
        else:
            child_count = self.child_counter(student_node)
            if child_count == 0:
                if self.Root == student_node:
                    del student_node
                    self.Root = None
                    return
                if student_node.parent.right == student_node:
                    student_node.parent.right = None
                else:
                    student_node.parent.left = None
                del student_node
                return

            student_node_parent = student_node.parent

            if child_count == 1:
                if student_node.left != None:
                    student_node_child = student_node.left
                else:
                    student_node_child = student_node.right
                if self.Root == student_node:
                    self.Root = student_node_child
                    student_node_child.parent = None
                else:
                    if student_node_parent.left == student_node:
                        student_node_parent.left = student_node_child
                        student_node_child.parent = student_node_parent
                    else:
                        student_node_parent.right = student_node_child
                        student_node_child.parent = student_node_parent
                del student_node


            elif child_count == 2:
                successor = student_node.right

                while successor.left != None:
                    successor = successor.left

                if successor.right != None:
                    if successor.parent.right == successor:
                        successor.parent.right = successor.right
                    else:
                        successor.parent.left = successor.right
                    successor.right.parent = successor.parent
                else:
                    if successor.parent.left == successor:
                        successor.parent.left = None
                    else:
                        successor.parent.right = None
                if self.Root != student_node:
                    if student_node.parent.left == student_node:
                        student_node.parent.left = successor
                    else:
                        student_node.parent.right = successor

                successor.parent = student_node.parent
                successor.left = student_node.left
                if successor.left != None:
                    successor.left.parent = successor
                successor.right = student_node.right
                if successor.right != None:
                    successor.right.parent = successor
                if self.Root == student_node:
                    self.Root = successor
                del student_node

        
    def child_counter(self, student_node):
        '''
        Returns the number of child nodes that student_node has
        '''
        child_count = 0
        if student_node.left != None:
            child_count += 1
        if student_node.right != None:
            child_count += 1
        
        return child_count


    def update_gpa(self, student_id, new_gpa) -> None:
        '''
        Updates the GPA of a student.
        '''
        student_node = self.search(student_id)
        if student_node == None:
            return
        else:
            student_node.GPA = new_gpa


    def update_name(self, student_id, new_name) -> None:
        """
        Updates the name of a student.
        """
        student_node = self.search(student_id)
        if student_node == None:
            return
        else:
            student_node.name = new_name


    def update_student_id(self, old_id, new_id) -> None:
        """
        Updates the student ID. This requires special handling to maintain tree structure.
        """
        if self.search(new_id) != None:
            print("ID already exists in tree")
            return
        student_copy = self.search(old_id)
        if student_copy == None:
            return
        student_name = student_copy.name
        student_GPA = student_copy.GPA
        self.delete(old_id)
        self.insert(new_id, student_name, student_GPA)


    def generate_report(self, student_id) -> str:
        """
        Generates a full report for a student.
        In the format of: Student ID: {student_id}, Name: {student.name}, GPA: {student.GPA}
        Otherwsie, print: No student found with ID {student_id}
        """
        found_student = self.search(student_id)
        if (found_student != None):
            report_string = "Student ID: {}, Name: {}, GPA: {}".format(found_student.student_id, found_student.name, found_student.GPA)
        else:
            report_string = "No student found with ID {}".format(student_id)
        return report_string


    def find_max_gpa(self) -> float:
        """
        Finds the maximum GPA in the tree.
        """
        inorder_list = self.inorder()
        max_gpa = 0
        for i in inorder_list:
            if i.GPA > max_gpa:
                max_gpa = i.GPA
        return max_gpa


    def find_min_gpa(self) -> float:
        """
        Finds the minimum GPA in the tree.
        """
        inorder_list = self.inorder()
        min_gpa = self.find_max_gpa()
        for i in inorder_list:
            if i.GPA < min_gpa:
                min_gpa = i.GPA
        return min_gpa


    def levelorder(self, level=None) -> list:
        """
        Performs a level order traversal of the tree. If level is specified, returns all nodes at that level.
        """
        if self.Root == None:
            return []
        traversal_queue = []
        level_order_lists = []
        level_order_lists_combined = []
        traversal_queue.insert(0, self.Root)
        while len(traversal_queue) > 0:
            current_queue_length = len(traversal_queue)
            level_list = []
            for i in range(current_queue_length):
                current_node = traversal_queue.pop()
                level_list.append(current_node)
                if current_node.left != None:
                    traversal_queue.insert(0, current_node.left)
                if current_node.right != None:
                    traversal_queue.insert(0, current_node.right)

            level_order_lists.append(level_list)
            level_order_lists_combined += level_list
  
        if level == None:
            return level_order_lists_combined
        elif level not in range(len(level_order_lists)):
            print("Level not in tree range")
            return []
        else:
            return level_order_lists[level]


    def inorder(self) -> list:
        """
        Performs an in-order traversal of the tree.
        """
        node = self.Root
        node_stack = []
        inorder_list = []

        while node != None or len(node_stack) > 0:
            while node != None:
                node_stack.append(node)
                node = node.left
            popped_node = node_stack.pop()
            inorder_list.append(popped_node)
            node = popped_node.right

        return inorder_list


    def is_valid(self) -> bool:
        """
        Checks if the tree is a valid Binary Search Tree. Return True if it is a valid BST, False or raise Exception otherwise.
        """
        inorder_list = self.inorder()
        for i in range(1, len(inorder_list)):
            if inorder_list[i-1].student_id > inorder_list[i].student_id:
                return False
        return True