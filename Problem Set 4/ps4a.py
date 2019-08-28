# Problem Set 4A
# Name: abode118

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 0:
        return []
    
    if len(sequence) == 1:
        return [sequence]

    else:
        list = []
        for i in range(len(sequence)):
            first = sequence[i] #for each letter in sequence
            remaining = sequence[:i] + sequence [i+1:] #remaining letters
            for p in get_permutations(remaining): #get permutations for remaining
                list.append(first + p) #add original letter to each permutation
        return list

get_permutations("abcd")

"""
#Adding to lists
list = ["a","b"]
list += ('c'+'d')
print(list)

list = ["a","b"]
list += ['c'] + ['d']
print(list)

list = ["a","b"]
list.append('c'+'d')
print(list)

list = ["a","b"]
list.append(["c"] + ["d"])
print(list)
"""

    
if __name__ == '__main__':
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print("/")
    
    example_input = 'def'
    print('Input:', example_input)
    print('Expected Output:', ['def', 'edf', 'efd', 'dfe', 'fed', 'fde'])
    print('Actual Output:', get_permutations(example_input))
    print("/")
    
    example_input = 'rot'
    print('Input:', example_input)
    print('Expected Output:', ['rot', 'rto', 'otr', 'ort', 'tor', 'tro'])
    print('Actual Output:', get_permutations(example_input))
    print("/")
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)