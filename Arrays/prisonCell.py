def prisonAfterNDays(cells, N):
    """
                                GOOD TO REVIEW

    There are 8 prison cells in a row, and each cell is either occupied or vacant.

    Each day, whether the cell is occupied or vacant changes according to the 
    following rules:

    - If a cell has two adjacent neighbors that are both occupied or both vacant, 
    then the cell becomes occupied.
    - Otherwise, it becomes vacant.

    (Note that because the prison is a row, the first and the last cells in the 
    row can't have two adjacent neighbors.)

    We describe the current state of the prison in the following way: 
    cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

    Given the initial state of the prison, return the state of the prison after 
    N days (and N such changes described above.)

    IDEA: [This isn't the naive approach]
    - There will ultimately be a repitition of the stepping between every iteration.
    - We need to find the length of the cycle. 
    - Basically, convert the current state of cells to a string, and add that to 
    a dictionary where the key is the stringified representation and the value is
    the number of iterations to get to that state.
    - If a stringified representation already exists in the dictionary, then we
    have found the cycle.
    - The cycle length will thus be the current index - dictionary[string of current state]
    - Then, we know that we just need to call prisonAfterNDays on cells, with 
    N = (N - current index) % cycle_len. We subtract by the current index because...
        - Let's take an example to explain this. 
        - Let's say the length of the cycle is 4. Say we would have found the
        stringified state in the dictionary when current index = 5. The string
        would have a value of 1 in the dictionary. So the cycle would be 
        1 -> 2 -> 3 -> 4 -> (5 == 1).
        - Now, if we want to find the 11th entry, then that will be the 3rd entry. 
         (0) (1 2 3 4) (5 6 7 8) (9 10 11 12), 1 == 5 == 9. (0 == 4) If we found the 
         repitition on index 5, then we need to 'offset' the cycle. 
        - Since cycle_len = 4, then we can get the 3rd entry by doing (11 - 5) % 4 = 2 
        (3rd entry by 0 indexing)
    """
    seen = {}

    for i in range(N):
        cell_str = str(cells)

        if cell_str in seen:
            cycle_len = i - seen[cell_str]
            return prisonAfterNDays(cells, (N - i) % cycle_len)
        else:
            seen[cell_str] = i
            cells = step(cells)

    return cells


def step(cells):
    temp = cells[:]
    for i in range(1, len(temp) - 1):
        if cells[i - 1] == cells[i + 1]:
            temp[i] = 1
        else:
            temp[i] = 0

    temp[0] = temp[-1] = 0
    return temp
