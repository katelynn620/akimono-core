# �˗��ڍו\�� 2005/01/06 �R��

DataRead();
CheckUserPass();
RequireFile('inc-req.cgi');
RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>���˗���</BIG><br><br>";

$i=SearchReqIndex($Q{no});
OutError('�w�肳�ꂽ�˗��͑��݂��܂���') if ($i==-1);
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
$TDB�˗��i
$TDB��V�i
$TDB�˗���
$TDB���
$TDB����
$TRE
STR

	$tex.='<tr><td>';
	if ($prn > 0) {
	$tex.=GetTagImgItemType($prn).$ITEM[$prn]->{name}.' '.$pr.$ITEM[$prn]->{scale};
	$tex.='<br><small>(�艿 '.GetMoneyString($ITEM[$prn]->{price} * $pr).')</small>';
	} else {
	$tex.='���� '.GetMoneyString($pr);
	}
	$tex.='<td>';
	if ($itemno > 0) {
	$tex.=GetTagImgItemType($itemno).$ITEM[$itemno]->{name}.' '.$num.$ITEM[$itemno]->{scale};
	$tex.='<br><small>(�艿 '.GetMoneyString($ITEM[$itemno]->{price} * $num).')</small>';
	} else {
	$tex.='���� '.GetMoneyString($num);
	}
	$tex.=defined($id2idx{$id}) ?'<td>'.$DT[$id2idx{$id}]->{shopname} : '<td>�Ȃ�';
	$tex.=defined($id2idx{$mode}) ? "<td><SPAN>�B��</SPAN>" : '<td> ';
	$tex.='<td>����'.GetTime2HMS($REQ[$i]->{tm}-$NOW_TIME);
$tex.=$TRE.$TBE;
}

sub ReqEnd
{
$disp.=$AucImg.'���̎���͂����B������Ă邺�B�܂���낵�����ނȁB<br><br>'.$tex;
}

sub ReqLast
{
if ($id != $DT->{id}) {
	# �˗��B���t�H�[��
	$disp.=<<STR;
$AucImg
���̈˗������ܒB�����邩���H<br><br>
$tex
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="req-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="plus">
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$no">
<BIG>���˗��B��</BIG>�F���̈˗���
 <INPUT TYPE=SUBMIT VALUE='�B������'>
</FORM>
STR
} else {
	# ��艺��
	$disp.=<<STR;
$AucImg
���̈˗��͂܂��B������Ă��Ȃ�����艺����̂����H<br><br>
$tex
<hr width=500 noshade size=1>
<FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="req-s">
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="end">
<INPUT TYPE=HIDDEN NAME=id VALUE="$DT->{id}">
<INPUT TYPE=HIDDEN NAME=idx VALUE="$no">
<BIG>���˗����~</BIG>�F���̈˗���
 <INPUT TYPE=SUBMIT VALUE='��艺����'>
</FORM>
STR
	}
}

