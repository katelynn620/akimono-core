use utf8;
# 移転フォーム 2005/01/06 由來

OutError(l('使用不可です')) if !$MOVETOWN_ENABLE || !$TOWN_CODE;
my $townmaster=ReadTown($TOWN_CODE,'getown');
OutError(l('使用不可です')) if !$townmaster;

DataRead();
CheckUserPass();

OutError(l('移転可能な街が見つかりません')) if !$Q{towncode};
$disp.=GetMoveShopForm($Q{towncode});
OutSkin();
1;

sub GetMoveShopForm
{
	my($towncode)=@_;
	
	my($town)=ReadTown($towncode);
	return '<b>'.l('移転可能な街が見つかりません').'</b>' if !$town;
	
	my $disp="";
	
	my $dist=GetTownDistance($townmaster->{position},$town->{position});
	my $movetime=GetMoveTownTime($DT,$townmaster,$town);
	
	$disp.=$TB;
	$disp.="$TR$TDB".l("移転先")."$TD$town->{name}$TRE";
	$disp.="$TR$TDB".l("コメント")."$TD$town->{comment}$TRE";
	$disp.="$TR$TDB".l("距離")."$TD".($dist*80)."m$TRE";
	$disp.="$TR$TDB".l("移動時間")."$TD".GetTime2HMS($movetime).' （'.l('予定').'）'.$TRE;
	$deny=0;
	
	sub GetMarkDeny
	{
		$deny=1,return l(" ←条件を満たしていません") if ($_[0]);
		return "";
	}
	my @flag=();
	push(@flag,l("以前の移転から 10 日以上").GetMarkDeny($NOW_TIME-GetUserDataEx($DT,'_so_move_in')<864000));	#追加
	push(@flag,l("資金 %1 以上",GetMoneyString($town->{allowmoney})).GetMarkDeny($town->{allowmoney}>$DT->{money}+$DT->{moneystock})) if $town->{allowmoney} ne '';
	push(@flag,l("資金 %1 以下",GetMoneyString($town->{denymoney})).GetMarkDeny($town->{denymoney}<$DT->{money}+$DT->{moneystock}))  if $town->{denymoney} ne '';
	push(@flag,l("ギルド")." ".join("/",map{GetTagImgGuild($_,1,1)}split(/\W/,$town->{allowguild})).($town->{onlyguild} ? '':l('およびギルド無所属'))." ".l("のみ").GetMarkDeny($DT->{guild} ne '' && !scalar(grep($_ eq $DT->{guild},split(/[^\w]+/,$town->{allowguild}))))) if $town->{allowguild} ne '';
	push(@flag,l("ギルド")." ".join("/",map{GetTagImgGuild($_,1,1)}split(/\W/,$town->{denyguild})).($town->{onlyguild} ? ' '.l('およびギルド無所属'):'')." ".l("以外").GetMarkDeny($DT->{guild} ne '' && scalar(grep($_ eq $DT->{guild},split(/[^\w]+/,$town->{denyguild}))))) if $town->{denyguild} ne '';
	push(@flag,l("トップ獲得回数 %1 回以上",$town->{allowtopcount}).GetMarkDeny($town->{allowtopcount}>$DT->{rankingcount})) if $town->{allowtopcount} ne '';
	push(@flag,l("トップ獲得回数 %1 回以下",$town->{denytopcount}).GetMarkDeny($town->{denytopcount}<$DT->{rankingcount}))  if $town->{denytopcount} ne '';
	push(@flag,l("開業期間 %1 以上",GetTime2HMS($town->{allowfoundation})).GetMarkDeny($town->{allowfoundation}>$NOW_TIME-$DT->{foundation})) if $town->{allowfoundation} ne '';
	push(@flag,l("開業期間 %1 以下",GetTime2HMS($town->{denyfoundation})).GetMarkDeny($town->{denyfoundation}<$NOW_TIME-$DT->{foundation}))  if $town->{denyfoundation} ne '';
	push(@flag,l("ギルド所属のみ")." ".GetMarkDeny($DT->{guild} eq '')) if $town->{onlyguild} ne '';
	push(@flag,l("ギルド無所属のみ")." ".GetMarkDeny($DT->{guild} ne '')) if $town->{noguild} ne '';
	push(@flag,l("職業")." ".join("/",map{$JOBTYPE{$_}}split(/\W+/,$town->{allowjob})).($town->{onlyjob} ? '':' '.l('および職業不定'))." ".l("のみ").GetMarkDeny($DT->{job} ne '' && !scalar(grep($_ eq $DT->{job},split(/\W+/,$town->{allowjob}))))) if $town->{allowjob} ne '';
	push(@flag,l("職業")." ".join("/",map{$JOBTYPE{$_}}split(/\W+/,$town->{denyjob})).($town->{onlyjob} ? ' '.l('および職業不定'):'')." ".l("以外").GetMarkDeny($DT->{job} ne '' && scalar(grep($_ eq $DT->{job},split(/\W+/,$town->{denyjob}))))) if $town->{denyjob} ne '';
	push(@flag,l("職業店舗のみ")." ".GetMarkDeny($DT->{job} eq '')) if $town->{onlyjob} ne '';
	push(@flag,l("職業不定店舗のみ")." ".GetMarkDeny($DT->{job} ne '')) if $town->{nojob} ne '';
	$disp.="$TR$TDB移転条件$TD・".join("<br>・",@flag)."$TRE" if scalar(@flag);
	$disp.=$TBE;
	
	return $disp if $deny;
	$disp.=<<"HTML";
		<hr width=500 noshade size=1>
		<form action="action.cgi" $METHOD>
		<input type=hidden name=key value="move-s">
		$USERPASSFORM
		<input type=hidden name=towncode value="$towncode">
		$TB$TR
		$TDB${\l('移転先での名前(ID)')}$TD<input type=text name=name value="$DT->{name}">(${\l('半角全角OK')})$TRE
		$TR$TDB現在のパスワード$TD<input type=password name=pass value="">$TRE$TBE
		<br><input type=submit value="${\l('移転手続開始')}">
		</form>
		<hr width=500 noshade size=1>
		<table><tr><td>${\l('移転で引き継がれないデータは下記の通りです。それ以外はほぼそのまま引き継がれます。')}
		<ul>
		<li>${\l('前期の順位情報')}
		<li>${\l('届いていた手紙（全て破棄）')}
		</ul>
		${\l('以下の場合は移転の際店舗データが一部失われます。')}
		<ul>
		<li>${\l('システム改造等で店舗データに互換性がない場合')}
		</ul>
		${\l('以下の場合は移転できません。')}
		<ul>
		<li>${\l('移転先が満員の場合')}
		<li>${\l('移転先に同じ名前(ID)や店舗名がある場合')}
		</ul></td></tr></table>
HTML
	return $disp;
}

