# �X���\�� 2005/01/06 �R��

if(!$GUEST_USER && !$MOBILE)
{
	my $tm=$NOW_TIME-$DT->{time};
	if($tm<0)
	{
		$tm=-$tm;
		$tm='�s���\�܂ł��� '.GetTime2HMS($tm);
	}
	else
	{
		$tm=$MAX_STOCK_TIME if $tm>$MAX_STOCK_TIME;
		$tm=GetTime2HMS($tm);
	}
	my $rankmsg=GetRankMessage($DT->{rank});
	my $moneymsg=GetMoneyString($DT->{money});
	$disp.=<<STR;
	$TB$TR
	$TD
	<SPAN>RANK</SPAN> ${\($id2idx{$DT->{id}}+1)}$TDE
	$TD<SPAN>�X���F</SPAN>$DT->{shopname}$TDE
	$TD<SPAN>�_���F</SPAN>$DT->{point}$TDE
	$TD<SPAN>�����F</SPAN>$moneymsg$TDE
	$TD<SPAN>���ԁF</SPAN>$tm$TDE
	$TRE$TBE
<hr width=500 noshade size=1>
STR
}
1;
