# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

p_hp = 50
b_hp = 50
MAX_HP = 50

# SECURITY AUDIT:
# The hardcoded SECRET_CODE and cheat logic were removed
# because they created a backdoor vulnerability.

def attack():
    global b_hp

# ATTACK LOGIC:
# The original function printed that 10 damage was dealt
# but did not reduce the boss's health.
# Fix: subtract 10 from b_hp when attack() is called.
    b_hp -= 10

    if b_hp < 0:
        b_hp = 0

    print("You deal 10 damage!")


def heal():
    global p_hp

 # HEALING GUARDRAILS:
 # The original function could heal above 50 HP
# or heal a player whose HP was 0 or less.
# Fix: prevent healing when defeated and cap HP at MAX_HP.
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return

    p_hp += 20

    if p_hp > MAX_HP:
        p_hp = MAX_HP

    print(f"Healed! HP is now {p_hp}")


# --- Simple Game Loop ---

# WIN CONDITION:
# When the boss reaches 0 HP, display "Victory!"
# and terminate the loop.

while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
    choice = input("Action [a]ttack, [h]eal: ").lower()

    if choice == 'a':
        attack()

    elif choice == 'h':
        heal()

    else:
        print("Invalid choice! Please choose 'a' or 'h'.")
        continue

    if b_hp <= 0:
        print("Victory!")
        break

    p_hp -= 10

if p_hp <= 0:
    print("Game Over!")
