<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# BoardR - Task Organizing System

_Part 4_

## 1. Description

**BoardR** is a task-management system which will evolve in the next several weeks. During the course of the project, we will follow the best practices of `Object-Oriented Programming` and `Design`.

## 2. Goals
- Practice **Composition** and **Has-A Relationship** by introducing a `user` as an instance of a class `User`. Refactor where necessary.
- Practice **Multiple Inheritance** - we will create `EditableBoard` and `ReadonlyBoard`

## 3. Class User

### Description

Instances of this class will be used to provide information about the user who is working on a given `task`.

### Initializer & Attributes

- **username**: _str_; should not be empty and should be unique
- **email**: _str_; should contain the symbol `@`
- **assigned_tasks**: _list_; the tasks assigned to this user. Should be maximum **3 tasks** on status `TODO` or `IN_PROGRESS`.

### Properties

- **username**: _str_ - getter-only
- **email**: _str_ - getter and setter
- **assigned_tasks**: _tuple_ - getter-only
- **capacity**: _int_ - returns how many more tasks could be assigned to this user

> **Hint I**: To ensure the uniqueness of the username, consider adding a collection of all users in the Board.
>

### Methods

- `advance_task_status(task)` - advances the `status` of a task if this user is the assignee of the task and the task is either on status `TODO` or on status `IN_PROGRESS` e.g. from `TODO` to `IN_PROGRESS` or from `IN_PROGRESS` to `DONE`.

> **Hint II** - For this method consider reusing the `advance_status()` method in the **BoardItem** class
> 

- `receive_task(task)` - adds the task to the collection of `assigned_tasks` of this user. If there is no capacity, raise ValueError.

- `remove_task(task)` - removes a task from the collection of assigned tasks if it exists, if not, raise ValueError.

> **Hint III** - Think about refactoring other parts of the code to make sure everything works as expected e.g. in class Task, the initializer accepts now assignee as an instance of `class User`, not a `str` and also you do not need the validation for the length of the username there.

> **Hint IV** - Think about the options you have to get a proper representation of the user for when you have already used it in the code e.g. in the logs/history.


#### Example

```python
steven = User("Steven", "steven@asd.com")
print(f"Steven capacity: {steven.capacity}") # 3
print(f"Steven assigned tasks: {steven.assigned_tasks}") # ()

task = Task('Test the application flow', steven, add_days_to_now(2))
steven.receive_task(task)
print(f"Steven capacity: {steven.capacity}") # 2
print(f"Steven assigned tasks: {[task.info() for task in steven.assigned_tasks]}") # Steven assigned tasks: ['Task (assigned to: Steven) Test the application flow, [Todo | 2023-07-16]']

steven.remove_task(task)
print(f"Steven capacity: {steven.capacity}") # 3
print(f"Steven assigned tasks: {steven.assigned_tasks}") # ()

```

## 4. Extend the Board Class

### Description

We will extend the Board so that it keeps information about the existing users.

### Attributes
- **_users**: _list_:  private attribute that would keep all existing users.

### Properties

- **team_capacity**: _int_: will return a number of all tasks that the team can handle with the existing users

### Methods

- **add_user(username, email)** - accept `username` and `email` as parameters and creates the user. If the **username** exists, raise ValueError. After validating the username authenticity and creating the user, we have to make sure the information for the existing users is updated in the collection of users.

- **reassign_task(task, new_assignee)** - the task is reassigned to `new_assignee`, removed from the **assigned_tasks** collection of the
 `current_assignee`. If the task does not exist or the assignee tries to assign the task to themselves raise ValueError. When reassigning tasks, they are always moved to the new `assignee` on status **TODO**. 

```python
board = Board()
steven = board.add_user("Steven", "steven@asd.bg")
task = Task('Test the application flow', steven, add_days_to_now(2))
steven.receive_task(task)
print(f"Capacity of the team: {board.team_capacity}") # Capacity of the team: 2

peter = board.add_user("Peter", "peter@asd.bg")
print(f"Capacity of the team: {board.team_capacity}") #Capacity of the team: 5
```

> **Hint I** - For reverting the status think about reusing the method `revert_status` in **BoardItem**.

Test code Input:
```python
board = Board()
steven = board.add_user("Steven", "steven@asd.bg")
task1 = Task('Test the application flow', steven, add_days_to_now(2))
steven.receive_task(task1)
board.add_item(task1)
print(f"Capacity of the team: {board.team_capacity}")
peter = board.add_user("Peter", "peter@asd.bg")
print(f"Capacity of the team: {board.team_capacity}")
print("============================================")
task2 = Task('Fix authentication', steven, add_days_to_now(2))
board.add_item(task2)
peter.receive_task(task2)
print(f"Capacity of the team: {board.team_capacity}")
print(task1.status)
steven.advance_task_status(task1)
print(task1.status)
board.reassign_task(task1, peter)
print(f"Steven assigned tasks: {steven.assigned_tasks}")
print(f"Peter assigned tasks: {[task.info() for task in peter.assigned_tasks]}")
print(task1.status)
peter.advance_task_status(task1)
print(task1.status)
peter.advance_task_status(task1)
print(task1.status)
print(f"Capacity of the team: {board.team_capacity}")
print(task1.history())
```

```python
Capacity of the team: 2
Capacity of the team: 5
============================================
Capacity of the team: 4
Todo
In progress
Steven assigned tasks: ()
Peter assigned tasks: ['Task (assigned to: Peter) Fix authentication, [Todo | 2023-07-16]', 'Task (assigned to: Peter) Test the application flow, [Todo | 2023-07-16]']
Todo
In progress
Done
Capacity of the team: 5
[07/14/2023, 16:25:58] Task created: Test the application flow
[07/14/2023, 16:25:58] Assignee changed from Steven to Steven
[07/14/2023, 16:25:58] Status changed from Todo to In progress
[07/14/2023, 16:25:58] Status changed from In progress to Todo
[07/14/2023, 16:25:58] Assignee changed from Steven to Peter
[07/14/2023, 16:25:58] Status changed from Todo to In progress
[07/14/2023, 16:25:58] Status changed from In progress to Done

```

## 5. Editable and Readonly Board
We will design the following two classes:
**EditableBoard**
    - `add_item()`
    - `remove_item()`
    - `count`
**ReadonlyBoard**
    - `add_item()`
    - `count`
One approach would be to subclass **EditableBoard** from **ReadonlyBoard** and add the `remove_item` method. This is ok, but we will practice another technique here - **Multiple Inheritance**.  
We need a class that provides each piece of functionality:
1. `Board`
    - initializer - initializes the `_items` collection
    - count property - returns the number of items in the `_items` collection
2. `CanAddItem`
    - `add_item(item: BoardItem)` - checks if this item exists, and if not, add it to the `_items` collection
3. `CanRemoveItem`
    - `remove_item(item: BoardItem)` - removes the item from `_items` collection

**Note** - neither `CanAddItem`, nor `CanRemoveItem` can exist individually - they trust that a class that provides `_items` will inherit them

CanRemoveItem example:
```python
class CanRemoveItem:
    def remove_item(self, item: BoardItem):
        # remove the item from self._items
```

Now that we have the building blocks, we can create the `Editable` and `Readonly` boards
- `ReadonlyBoard` = `Board` + `CanAddItem`
- `EditableBoard` = `Board` + `CanAddItem` + `CanRemoveItem`

ReadonlyBoard example:
```python
class ReadonlyBoard(Board, CanAddItem):
    pass # no additional code is really required here. All the functionality is inherited
```

Test code:
```python
issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))

readonly_board = ReadonlyBoard()
steven = readonly_board.add_user("Steven", "steven@asd.bg")
task = Task('Dont refactor anything', steven, add_days_to_now(2))

readonly_board.add_item(issue)  # method from CanAddItem
readonly_board.add_item(task)
print(readonly_board.count)  # 2     # property from Board

editable_board = EditableBoard()
editable_board.add_item(issue)  # method from CanAddItem
editable_board.remove_item(issue)  # method from CanRemoveItem
print(editable_board.count)  # 0     # property from Board
```


## 6. Optional - Refactor the Project structure
- We have more than 10 files in our project, and the structure is starting to become a little messy
- If you haven't created any folders so far, all the files will be at one place and it will begin to look confusing
- If you have written your files in organized folders, you can skip this step
- Otherwise, try to logically organize the files. One possible approach is:
    
```none
board/
   board.py
   can_add_item.py
   can_remove_item.py
   editable_board.py
   readonly_board.py
board_items/
   board_item.py
   issue.py
   item_status.py
   task.py
event_logging/
   event_log.py
user/
   user.py
main.py
```

- **Note** import paths will change, for example:   
    `from readonly_board import ReadonlyBoard`   
    will become  
    `form board.readonly_board import ReadonlyBoard`  