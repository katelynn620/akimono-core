use utf8;
# 依頼詳細表示 2005/01/06 由來

DataRead();
CheckUserPass();
RequireFile('inc-req.cgi');
RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>●".l('依頼所')."</BIG><br><br>";

$i=SearchReqIndex($Q{no});
OutError(l('指定された依頼は存在しません')) if ($i==-1);
my($no,$id,$itemno,$num,$prn,$pr,$mode)=($REQ[$i]->{no},$REQ[$i]->{id},$REQ[$i]->{itemno},$REQ[$i]->{num},$REQ[$i]->{prn},$REQ[$i]->{pr},$REQ[$i]->{mode});
ReqDataSet();
ReqEnd() if defined($id2idx{$mode});
ReqLast() if !defined($id2idx{$mode});

OutSkin();
1;


sub ReqDataSet
{
$tex=<<STR;
$TB$TR
$TDB${\l('依頼品')}
$TDB${\l('報酬品')}
$TDB${\l('依頼者')}
$TDB${\l('状態')}
$TDB${\l('期限')}
$TRE
STR

	$tex.='<tr><td>';
	if ($prn > 0) {
	$tex.=GetTagImgItemType($prn).$ITEM[$prn]->{name}.' '.$pr.$ITEM[$prn]->{scale};
	$tex.='<br><small>('.l('定価').' '.GetMoneyString($ITEM[$prn]->{price} * $pr).')</small>';
	} else {
	$tex.=l('資金').' '.GetMoneyString($pr);
	}
	$tex.='<td>';
	if ($itemno > 0) {
	$tex.=GetTagImgItemType($itemno).$ITEM[$itemno]->{name}.' '.$num.$ITEM[$itemno]->{scale};
	$tex.='<br><small>('.l('定価').' '.GetMoneyString($ITEM[$itemno]->{price} * $num).')</small>';
	} else {
	$tex.=l('資金').' '.GetMoneyString($num);
	}
	$tex.=defined($id2idx{$id}) ?'<td>'.$DT[$id2idx{$id}]->{shopname} : '<td>'.l('なし');
	$tex.=defined($id2idx{$mode}) ? "<td><SPAN>".l('達成')."</SPAN>" : '<td> ';
	$tex.='<td>'.l("あと%1",GetTime2HMS($REQ[$i]->{tm}-$NOW_TIME));
$tex.=$TRE.$TBE;
}

sub ReqEnd
{
$disp.=$AucImg.l('この取引はもう達成されてるぜ。またよろしく頼むな。').'<br><br>'.$tex;
}

sub ReqLast
{
if ($id != $DT->{id}) {
	# 依頼達成フォーム
	$disp.=<<STR;
$AucImg
${\l('この依頼をいま達成するかい？')}<br><br>
$tex
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="req-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="plus">
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$no">
<BIG>●${\l('依頼達成')}</BIG>：${\l('この依頼を')}
 <INPUT TYPE=SUBMIT VALUE='${\l('達成する')}'>
</FORM>
STR
} else {
	# 取り下げ
	$disp.=<<STR;
$AucImg
${\l('この依頼はまだ達成されていないが取り下げるのかい？')}<br><br>
$tex
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="req-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="end">
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$no">
<BIG>●${\l('依頼中止')}</BIG>：${\l('この依頼を')}
 <INPUT TYPE=SUBMIT VALUE='${\l('取り下げる')}'>
</FORM>
STR
	}
}

