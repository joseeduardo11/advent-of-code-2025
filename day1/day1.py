""" --- Day 1: Secret Entrance ---
The Elves have good news and bad news.

The good news is that they've discovered project management! This has given them the tools they need to prevent their usual Christmas emergency. For example, they now know that the North Pole decorations need to be finished soon so that other critical tasks can start on time.

The bad news is that they've realized they have a different emergency: according to their resource planning, none of them have any time left to decorate the North Pole!

To save Christmas, the Elves need you to finish decorating the North Pole by December 12th.

Collect stars by solving puzzles. Two puzzles will be made available on each day; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the password seems to have been changed, so you can't get in. A document taped to the wall helpfully explains:

"Due to new security protocols, the password is locked in the safe below. Please see the attached document for the new combination."

The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order. As you turn the dial, it makes a small click noise as it reaches each number.

The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.

So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0.

Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0.

So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.

The dial starts by pointing at 50.

You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.

For example, suppose the attached document contained the following rotations:

L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
Following these rotations would cause the dial to move as follows:

The dial starts by pointing at 50.
The dial is rotated L68 to point at 82.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32.
Because the dial points at 0 a total of three times during this process, the password in this example is 3.

Analyze the rotations in your attached document. What's the actual password to open the door?

Your puzzle answer was 1064.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.

As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:

"Due to newer security protocols, please use password method 0x434C49434B until further notice."

You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

The dial starts by pointing at 50.
The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.

Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!

Using password method 0x434C49434B, what is the password to open the door? """


from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
content = (script_dir / 'input.txt').read_text()

""" if __name__ == '__main__':
    actual_pos = 50
    password = 0
    # Split content into lines
    lines = content.strip().split('\n')
#   lines = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']
    # Process each line
    for line in lines:
        direction, distance = line[0], int(line[1:])
       
        if direction == 'R':
            # Moving right: count how many times we cross 0
            # Starting from actual_pos, we cross 0 at positions 100, 200, 300, etc.
            crosses = (actual_pos + distance) // 100
            password += crosses
            actual_pos = (actual_pos + distance) % 100

        elif direction == 'L':
            # Moving left: count how many times we cross 0
            # We cross 0 going backwards from actual_pos
            new_pos = actual_pos - distance
            if new_pos < 0:
                # We crossed 0 at least once
                crosses = (abs(new_pos) + 99) // 100
                password += crosses
            actual_pos = new_pos % 100
    
    print(password)
 """

def count_zeros_in_rotation(start_pos, direction, steps):
    """
    Count how many times we hit position 0 when rotating.
    
    L = counterclockwise = decreasing position numbers
    R = clockwise = increasing position numbers
    """
    if steps == 0:
        return 0
    
    if direction == 'L':
        # Decreasing: we visit positions (start-1), (start-2), ..., (start-steps)
        # We hit 0 when (start-k) ≡ 0 (mod 100), i.e., k ≡ start (mod 100)
        # for k in {1, 2, ..., steps}
        
        if start_pos == 0:
            # We hit 0 at k = 100, 200, 300, ...
            return steps // 100
        else:
            # We hit 0 at k = start_pos, start_pos+100, start_pos+200, ...
            if start_pos <= steps:
                return (steps - start_pos) // 100 + 1
            else:
                return 0
    
    else:  # direction == 'R'
        # Increasing: we visit positions (start+1), (start+2), ..., (start+steps)
        # We hit 0 when (start+k) ≡ 0 (mod 100), i.e., k ≡ -start ≡ (100-start) (mod 100)
        # for k in {1, 2, ..., steps}
        
        if start_pos == 0:
            # We hit 0 at k = 100, 200, 300, ...
            return steps // 100
        else:
            # We hit 0 at k = (100-start_pos), (100-start_pos)+100, ...
            target = 100 - start_pos
            if target <= steps:
                return (steps - target) // 100 + 1
            else:
                return 0

def solve(input_text):
    """
    Parse input and calculate the password using method 0x434C49434B.
    """
    lines = input_text.strip().split('\n')
    
    position = 50  # Starting position
    total_zeros = 0
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        direction = line[0]  # 'L' or 'R'
        steps = int(line[1:])
        
        # Count zeros in this rotation
        zeros = count_zeros_in_rotation(position, direction, steps)
        total_zeros += zeros
        
        # Update position
        if direction == 'L':
            position = (position - steps) % 100
        else:  # direction == 'R'
            position = (position + steps) % 100
        
        print(f"{direction}{steps}: moved to {position}, hit 0 {zeros} time(s)")
    
    return total_zeros

# Example from the problem
example_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

print("Example:")

result = solve(content)
print(f"\nTotal times dial points at 0: {result}")
print("\n" + "="*50)
print("\nTo solve with your actual input, replace the input string above")
print("or read from a file:")
print("\n# with open('input.txt', 'r') as f:")
print("#     actual_input = f.read()")
print("#     result = solve(actual_input)")
print("#     print(f'Password: {result}')")
