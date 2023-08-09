@dice = qw(foxrib moqabj furilw setupl camped acitao slcrae romash 
		   nodesw hefiye onudtk tevign anedvz pinesh abilyt gkyleu);

my @board = &make_board(fy_shuffle(@dice));
$board = join "", @board;
$board =~ s/([^\n]{4})/$1\n/g;

print $board;

sub make_board {
	my @board, $i;
	$board[$i++] = substr $_, int rand length, 1 foreach @_;
	return @board;
} # make_board

sub fy_shuffle {
	my $i = @_;
	@_[$i, $_] = @_[$_, $i] for int rand(--$i + 1);
	return @_;
} # fy_shuffle
