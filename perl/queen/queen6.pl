for(0..14){$t[$_]="000000010000000";$t[7]="1"x15;substr($t[$_],$_,1)=substr(
$t[$_],14-$_,1)="1";@y=0..7;}for$x(@y){for$y(@y){$m[$x+($y*8)].=substr($t[7-
$y+$_],7-$x,8)for@y;}}$a=$b="0"x64;$d=-1;z($_)for@y;print join "\n",keys 
%r;sub z {my($p)=@_;my $o=$p+(8*++$d);($b&$m[$o]) ne $a?return $d--:{ 
substr($b,$o,1)="1"};$d==7?$r{$b}++:z($_)for @y;substr($b,$o,1)="0";$d--;}
