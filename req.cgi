use utf8;
# 依頼一覧表示 2005/01/06 由來

DataRead();
CheckUserPass(1);
RequireFile('inc-req.cgi');
RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>●".l('依頼所')."</BIG><br><br>";

$enum=0;
if ($REQNONE)
	{
	$disp.=<<STR;
	$TBT$TRT$TD$AucImg
	$TD<SPAN>${\l('依頼所の受付')}</SPAN><br>
	${\l('今のところ依頼はないぜ。依頼を出してみるかい？')}$TRE$TBE<br>
STR
	}
	else
	{
	ReqList();
	}
if (!$GUEST_USER && $enum < $REQUEST_CAPACITY)
	{
	$disp.=<<STR;
	<br>
	<FORM ACTION="action.cgi" $METHOD>
	<INPUT TYPE=HIDDEN NAME=key VALUE="req-f">
	$USERPASSFORM
	<INPUT TYPE=SUBMIT VALUE='${\l('新しい依頼書を作成する')}'>
	</FORM>
STR
	}
OutSkin();
1;


sub ReqList
{
$disp.=<<STR;
	$TBT$TRT$TD$AucImg
	$TD<SPAN>${\l('依頼所の受付')}</SPAN><br>
	${\l('これだけの依頼が出ているぜ。')}$TRE$TBE<br>
$TB$TR
$TDB${\l('依頼品')}
$TDB${\l('報酬品')}
$TDB${\l('依頼者')}
$TDB${\l('状態')}
$TDB${\l('期限')}
$TRE
STR

foreach my $i(0..$Scount)
{
	next unless defined($REQ[$i]->{no});
	my($no,$id,$itemno,$num,$prn,$pr,$mode)=($REQ[$i]->{no},$REQ[$i]->{id},$REQ[$i]->{itemno},$REQ[$i]->{num},$REQ[$i]->{prn},$REQ[$i]->{pr},$REQ[$i]->{mode});
	$disp.=$TR.$TD;
	if (!$GUEST_USER)
		{
		$disp.=($mode && $id == $DT->{id}) ? "<a href=\"action.cgi?key=req-s&mode=thank&idx=$no&$USERPASSURL\">" : "<a href=\"action.cgi?key=req-l&no=$no&$USERPASSURL\">";
		}
	if ($prn > 0)
		{
		$disp.=GetTagImgItemType($prn).$ITEM[$prn]->{name}.' '.$pr.$ITEM[$prn]->{scale};
		$disp.=    "</a>" if (!$GUEST_USER);
		$disp.='<br><small>('.l('定価').' '.GetMoneyString($ITEM[$prn]->{price} * $pr).')</small>';
		}
		else
		{
		$disp.=l('資金').' '.GetMoneyString($pr);
		$disp.=    "</a>" if (!$GUEST_USER);
		}
	$disp.=$TD;
	if ($itemno > 0)
		{
		$disp.=GetTagImgItemType($itemno).$ITEM[$itemno]->{name}.' '.$num.$ITEM[$itemno]->{scale};
		$disp.='<br><small>('.l('定価').' '.GetMoneyString($ITEM[$itemno]->{price} * $num).')</small>';
		}
		else
		{
		$disp.=l('資金').' '.GetMoneyString($num);
		}
	$disp.=($DT->{id} == $REQ[$i]->{id}) ? $TDB : $TD;
	$disp.=defined($id2idx{$id}) ? ($DT[$id2idx{$id}]->{shopname}) : 'なし';
	$disp.=defined($id2idx{$mode}) ? "$TD<SPAN>".l('達成')."</b></SPAN>" : "$TD ";
	$disp.="$TD".l("あと%1",GetTime2HMS($REQ[$i]->{tm}-$NOW_TIME));
	$enum++ if ($id == $DT->{id});	#出品数をカウント
	}
$disp.=$TRE.$TBE;
}

