for $p (0..14) {
	$t[$p] = "000000010000000"; $t[7] = "1"x15;
	substr($t[$p], $p, 1) = "1"; substr($t[$p], 14-$p, 1) = "1";
}

for $x (0..7) { for $y (0..7) {
	$m[$x+($y*8)] .= substr($t[7-$y+$_], 7-$x, 8) for 0..7;
} }

$b = "0" x 64; $a = $b;
&z($_, 0) for 0..7;
$s =~ s/([^\n]{8})/$1\n/g; print $s;

sub z {
	my ($p,$d) = @_;
	($b & $m[$p+($d*8)]) ne $a?return:eval 'substr($b, $p+($d*8), 1) = "1"';
	$d == 7?eval '$s .= "$b\n\n" if $s !~ /$b/':&z($_, $d+1) for 0..7;
	substr($b, $p+($d*8), 1) = "0";
}
