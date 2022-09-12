use utf8;
# ギルドコマンド 2005/01/06 由來

my $usetime=3*60*60;
$disp.='<hr width=500 noshade size=1>';
GuildFundF();
$disp.='<hr width=500 noshade size=1>';
Break();
my $checkok;
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{leadt} eq $MYDIR && $GUILD_DETAIL{$DT->{guild}}->{leader} == $DT->{id});
$ckeckok=1 if ($GUILD_DETAIL{$DT->{guild}}->{$MYDIR} == $DT->{id});
Force() if ($ckeckok);
1;

sub GuildFundF
{
	$stock=($DT->{money} - 100000);
	$disp.="<BIG>●".l('ギルド寄付')."</BIG>： ".l("資金の余裕がありません"),return if ($stock < 100000);
$disp.=<<STR;
	<form action="action.cgi" $METHOD>
	<INPUT TYPE=HIDDEN NAME=key VALUE="gd-s">
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=mode VALUE="fund">
	<BIG>●${\l('ギルド寄付')}</BIG>： $term[0]
	<SELECT NAME=cnt1>
	<OPTION VALUE="0" SELECTED>
STR
	$msg{1000}=1000;
	$msg{10000}=10000;
	$msg{100000}=100000;
	$msg{1000000}=1000000;
	$msg{$stock}="$stock(".l('最大額').")";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1000,10000,100000,1000000,$stock))
	{
		last if $stock<$cnt || $cnt==$oldcnt;
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
$disp.=<<STR;
	</SELECT>
	${\l('%1、もしくは %2',$term[1],$term[0])}
	<INPUT TYPE=TEXT SIZE=7 NAME=cnt2>$term[1]
	<INPUT TYPE=SUBMIT VALUE="${\l('寄付する')}">
	</FORM>
STR
}

sub Break
{
	$disp.="<BIG>●".l('ギルドブレイク')."</BIG>： ".l("肩書きがつかないと実行できません"),return if (!$DT->{user}{_so_e});
	$disp.='<BIG>●'.l('ギルドブレイク')."</BIG>： ".l('時間が足りません'),return if GetStockTime($DT->{time})<$usetime;
	$target="";
	foreach (keys(%GUILD))
	{
	$target.="<OPTION value=\"$_\">$GUILD{$_}->[$GUILDIDX_name]" if $GUILD_DATA{$_}->{money} > $GUILD_DATA{$DT->{guild}}->{money};
	}
	$disp.="<BIG>●".l('ギルドブレイク')."</BIG>： ".l("相手がいません"),return if (!$target);
$disp.=<<STR;
<form action="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="gd-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="break">
<BIG>●${\l('ギルドブレイク')}：</BIG>
<SELECT NAME=tg>
<OPTION value="">
$target
</SELECT>
${\l('に対して')}
<INPUT TYPE=SUBMIT VALUE="${\l('攻撃する')}">
STR
	$disp.="(".l('消費時間').":".GetTime2HMS($usetime).")</FORM>";
}

sub Force
{
	$disp.='<hr width=500 noshade size=1>';
	$disp.="<BIG>●".l('軍備増強')."</BIG>： ".l("肩書きがつかないと実行できません"),return if (!$DT->{user}{_so_e});
	$disp.='<BIG>●'.l('軍備増強').'</BIG>： '.l("時間が足りません"),return if GetStockTime($DT->{time})<$usetime;
	$disp.="<BIG>●".l('軍備増強')."</BIG>： ".l("増強の必要がありません"),return if ($GUILD_DATA{$DT->{guild}}->{atk} > 990);
$disp.=<<STR;
<form action="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="gd-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="force">
<BIG>●${\l('軍備増強')}：</BIG>
${\l('%1の攻撃力を',$GUILD{$DT->{guild}}->[$GUILDIDX_name])}
<INPUT TYPE=SUBMIT VALUE="${\l('強化する')}"> (${\l('ギルド資金4分の1消費')})
STR
	$disp.="(".l('消費時間').":".GetTime2HMS($usetime).")</FORM>";
}

