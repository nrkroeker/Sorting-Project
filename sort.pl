# Array to store user-inputted integers
@numbers = ();

# Method to print all the numbers in the array
sub printNumbers {
    foreach my $n (@numbers) {
        print "$n ";
    }
}

# Method to sort the numbers using Bubble sort
sub sortList {
    $length = scalar @numbers;
    for $i (0 .. $length) {
        for $j (0 .. $length - $i - 1) {
            if (@numbers[$j] < @numbers[$j + 1]) {
                $temp = @numbers[$j];
                @numbers[$j] = @numbers[$j + 1];
                @numbers[$j + 1] = $temp;
            }
        }
    }
}

# Retrieve input from the user and push it into the array
print "Please input 10 integers\n";
for $x (0 .. 9) {
    print "> ";
    my $newNumber = <STDIN>;
    chomp $newNumber; # Trim the newline from the user pressing enter
    push @numbers, $newNumber;
}
# Print the list of integers as inputted by the user
print "\nUnsorted list: ";
printNumbers();

# Sort the integers, and print them in sorted order
sortList();
print "\nSorted list: ";
printNumbers();