# �݈ʃ��X�g������ 2003/07/19 �R��

$disp.="<BIG>���V���F�݈ʃ��X�g</BIG><br><br>";

my @itemlist=();
my %msg;
my $bar;

foreach my $DT (@DT)
{
	my $shopname=$DT->{shopname};
	my $name=$DT->{name};
	my $count=$DT->{dignity};
	next if !$count;
	my $num=0;
	foreach(1..$#DIG_POINT)
	{
		last if $count<$DIG_POINT[$_];
		$num++;
	}
	$msg{$num}.=$shopname."�C ";
}

my $ret;
foreach (1..$#DIG_POINT) {
	$msg{$_} = substr($msg{$_},0,(length($msg{$_})-3)) if ($msg{$_});
	$ret=$TR.$TDB.DignityDefine($DIG_POINT[$_],2).$TD.$msg{$_}.$TRE.$ret;
}
$disp.="$TB$TR<td width=50>�݈�<td class=b width=570>�X��$TRE";
$disp.=$ret.$TBE;
1;
