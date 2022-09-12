use utf8;
# 店情報表示 2005/01/06 由來

if(!$GUEST_USER && !$MOBILE)
{
	my $tm=$NOW_TIME-$DT->{time};
	if($tm<0)
	{
		$tm=-$tm;
		$tm=l('行動可能まであと %1',GetTime2HMS($tm));
	}
	else
	{
		$tm=$MAX_STOCK_TIME if $tm>$MAX_STOCK_TIME;
		$tm=GetTime2HMS($tm);
	}
	my $rankmsg=GetRankMessage($DT->{rank});
	my $moneymsg=GetMoneyString($DT->{money});
	my $timestr = l('時間#A');
	$timestr =~ s/#A//g;
	$disp.=<<STR;
	$TB$TR
	$TD
	<SPAN>RANK</SPAN> ${\($id2idx{$DT->{id}}+1)}$TDE
	$TD<SPAN>${\l('店名')}：</SPAN>$DT->{shopname}$TDE
	$TD<SPAN>${\l('点数')}：</SPAN>$DT->{point}$TDE
	$TD<SPAN>${\l('資金')}：</SPAN>$moneymsg$TDE
	$TD<SPAN>$timestr：</SPAN>$tm$TDE
	$TRE$TBE
<hr width=500 noshade size=1>
STR
}
1;
