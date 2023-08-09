my $a = "00000001";
my $b = "00110000";

my $c = pack("B8", $a) ^ pack("B8", $b);

print $c . "\n";
