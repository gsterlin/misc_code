 $t[1] = "100000010000001";
 $t[2] = "010000010000010";
 $t[3] = "001000010000100";
 $t[4] = "000100010001000";
 $t[5] = "000010010010000";
 $t[6] = "000001010100000";
 $t[7] = "000000111000000";
 $t[8] = "111111111111111";
 $t[9] = $t[7];
$t[10] = $t[6];
$t[11] = $t[5];
$t[12] = $t[4];
$t[13] = $t[3]; 
$t[14] = $t[2];
$t[15] = $t[1];

for $x (0..7) {
	for $y (0..7) {
		my $str;
		$str .= pack "B8", substr($t[8-$y+$_], 7-$x, 8) for 0..7;
		$map[$x+($y*8)] = $str;
	} # for
} # for

$b = "0000000000000000000000000000000000000000000000000000000000000000";
$a = pack "B64", $b;

for (0..63) {
	&algo(1, $_);
} # for


sub algo {
	my $depth = shift;
	my $pos = shift;

	return if (pack("B64", $b) & $map[$pos]) ne $a;
	substr($b, $pos, 1) = "1";

	if ($depth == 8) {
		my $buya = $b;
		$buya =~ s/([^\n]{8})/$1\n/g;
		print "$buya\n";
		substr($b, $pos, 1) = "0";
		return;
	}

	foreach $xyz (0..63) {
		&algo($depth+1, $xyz);
	} # foreach

	substr($b, $pos, 1) = "0";
} # algo
