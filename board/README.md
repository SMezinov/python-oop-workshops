<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# BoardR - Task Organizing System

_Part 4_

## 1. Description

**BoardR** is a task-management system which will evolve in the next several weeks. During the course of the project, we will follow the best practices of `Object-Oriented Programming` and `Design`.

## 2. Goals


- Practice **Polymorphism** and **Duck Typing** - the two concepts are closely related in Python.
    - Polymorphism - override some of the methods in Task and Issue
    - Duck Typing - call the same method on a BoardItem object (could be a Task, could be an Issue) and dynamically execute the correct one
  
## 3. Task class

### Description

Instances of this class will be used to describe work that needs to be done. They extend the functionality of a board item by adding an **assignee** property.

### Initializer

- Parameters: `title` (_str_), `assignee` (_str_) and `due_date` (_date_)
- A new Task should have its initial status as `Todo`
- Example:

```
task = Task('Test the application flow', 'Steven', add_days_to_now(2))
print(task.title)      # Test the application flow
print(task.due_date)   # 2022-03-18
print(task.status)     # Todo
print(task.assignee)   # Steven
```

### Properties

- Inherits all props from **BoardItem**
- `assignee`: _str_, should never be empty, and its length should be between [5..30]

> **Hint**: When you implement the assignee setter, you can think about if there is a way to reuse recording EventLogs functionality from the base class
>
> **Hint II** - You will also need to find a way to start from `Todo` status instead of an `Open` status. The easiest approach is to pass the value to the `super()` initializer

### Methods

- Inherits all methods from **BoardItem**

#### Example

```
task = Task('Test the application flow', 'Steven', add_days_to_now(2))
task.advance_status()
task.advance_status()
task.assignee = 'Not Steven'
print(task.history())
```

#### Output

```
[03/16/2022, 16:52:07] Task created: Test the application flow, [Todo | 2022-03-18]
[03/16/2022, 16:52:07] Status changed from Todo to In progress
[03/16/2022, 16:52:07] Status changed from In progress to Done
[03/16/2022, 16:52:07] Assignee changed from Steven to Not Steven
```

## 4. Issue class

### Description

Instances of this class will be used to describe a problem that needs attention. Their status will start at `OPEN`.

### Initializer

- Parameters: `title` (_str_), `description` (_str_), dueDate (_date_)
- A new Issue should have its initial status as Open
- Example:

```
issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))
print(issue.description) # We need to test the flow!
```

### Properties

- Inherit all properties from BoardItem
  `description`: _str_ - if someone tries to assign an empty string to it, set to `No description`
  - Description can't be changed once set.

### Methods

- Inherits all methods from BoardItem

#### Example

```
issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))
issue.advance_status()
issue.due_date += timedelta(days = 1)
print(issue.history())
```

#### Output

```
[03/16/2022, 16:56:02] Issue created: App flow tests?, [Open | 2022-03-17]
[03/16/2022, 16:56:02] Status changed from Open to Todo
[03/16/2022, 16:56:02] DueDate changed from 2022-03-17 to 2022-03-18
```
## 5. Override BoardItem.info()

### Description

We will create separate `.info()` methods in Task and Issue. The one in task will provide additional information about the `assignee`, and the one in Issue will also display the `description`. We will enhance the base info the following way.
- task.info = asignee + super.info
- issue.info = description + super.info
- super.info is the info method defined in the base class
- sample code in `Issue`:
    ```
    def info(self):
        board_item_info = super().info() # obtain base class information
        
        return # Issue + description + board item info 
    ```
- to the same in Task class, but display `Task + assignee + board item info` instead
- **IMPORTANT NOTE**: if the initializer of the BoardItem class uses the `.info` method, you could run into troubles
    1. it will call the overriden `info` - the one that uses either `description` or `assignee` properties
    1. when it calls the overriden `info`, the initializer for `Task` and `Issue` have not yet executed
    1. so neither `description`, nor `assignee` exists at this point in time
    1. but the overriden `info` uses one of them ...
    1. ...
    1. **Runtime Error!**
    1. Remember, **be mindful if you use methods from the same class in an initializer**. Some other derived class may override them and cause problems.

- Run the following code in the main file:

    ```
    issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))
    task = Task('Dont refactor anything', 'Pesho', add_days_to_now(2))

    print(issue.info())
    print(task.info())
    ```
- If everything is ok, this is the expected output:
    ```none
    Issue (We need to test the flow!) App flow tests?, [Open | 2022-03-26]
    Task (assigned to: Pesho) Dont refactor anything, [Todo | 2022-03-27]
    ```

We also saw **Duck Typing** in action - the call to the `.info` from either `task` or `issue` objects.  
The **Duck Typing** will be much more obvious, if we rewrite the code like this - there will be no change in the output.
```
issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))
task = Task('Dont refactor anything', 'Pesho', add_days_to_now(2))

for board_item in [issue, task]:
    print(board_item.info()) # prints info like either an issue, or a task
```


## 6. Board class

The board class should continue to work as before without any changes.

In the next part of the project we will learn how the Board class will deal with two different types (Issue / Task) in an **abstract** way by focusing on the common attributes/methods that both classes possess.
