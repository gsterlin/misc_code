for $p (0..14) {
	$t[$p] = "000000010000000";
	$t[7] = "1"x15;
	substr($t[$p], $p, 1) = "1";
	substr($t[$p], 14-$p, 1) = "1";
}

for $x (0..7) {
	for $y (0..7) {
		$m[$x+($y*8)] .= substr($t[7-$y+$_], 7-$x, 8) for 0..7;
	}
}

$b = "0" x 64;
$a = $b;

$base = 64*64*64*64*64*64*64*64;
$x = 0;

&z($_, $d+1) for 0..63;

$s =~ s/([^\n]{8})/$1\n/g;
print $s;

sub z {
	my $p = shift;
	my $d = shift;
	$count++;

	my $progress = ($count / $base) * 100;
	
	if ($progress > $x) {
		print "$x\n";
		$x++;
	}

	return if ($b & $m[$p]) ne $a;
	substr($b, $p, 1) = "1";

	if ($d == 8) {
		$s .= "$b\n" if $s !~ /$b/;
	}
	else {
		&z($_, $d+1) for 0..63;
	}

	#$d == 8?eval '$s .= "$b|" if $s !~ /$b/':&z($_, $d+1) for 0..63;

	substr($b, $p, 1) = "0";
}
