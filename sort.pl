@numbers = ();

sub printNumbers {
    foreach my $n (@numbers) {
        print "$n ";
    }
}

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

print "Please input 10 integers\n";
for $x (0 .. 9) {
    print ">";
    my $newNumber = <STDIN>;
    chomp $newNumber;
    push @numbers, $newNumber;
}
print "\nUnsorted list: ";
printNumbers();

sortList();
print "\nSorted list: ";
printNumbers();