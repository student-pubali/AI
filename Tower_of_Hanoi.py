def TowerofHanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from source {source} to destination {destination}")
        return
    TowerofHanoi(n-1, source, auxiliary, destination)  # Move n-1 disks from source to auxiliary
    print(f"Move disk {n} from source {source} to destination {destination}")  # Move the nth disk
    TowerofHanoi(n-1, auxiliary, destination, source)  # Move n-1 disks from auxiliary to destination

# Number of disks
n = 4

# Solve the Tower of Hanoi problem
TowerofHanoi(n, 'A', 'B', 'C')
