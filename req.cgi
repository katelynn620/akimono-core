# �˗��ꗗ�\�� 2005/01/06 �R��

DataRead();
CheckUserPass(1);
RequireFile('inc-req.cgi');
RequireFile('inc-html-ownerinfo.cgi');

$disp.="<BIG>���˗���</BIG><br><br>";

$enum=0;
if ($REQNONE)
	{
	$disp.=<<STR;
	$TBT$TRT$TD$AucImg
	$TD<SPAN>�˗����̎�t</SPAN><br>
	���̂Ƃ���˗��͂Ȃ����B�˗����o���Ă݂邩���H$TRE$TBE<br>
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
	<INPUT TYPE=SUBMIT VALUE='�V�����˗������쐬����'>
	</FORM>
STR
	}
OutSkin();
1;


sub ReqList
{
$disp.=<<STR;
	$TBT$TRT$TD$AucImg
	$TD<SPAN>�˗����̎�t</SPAN><br>
	���ꂾ���̈˗����o�Ă��邺�B$TRE$TBE<br>
$TB$TR
$TDB�˗��i
$TDB��V�i
$TDB�˗���
$TDB���
$TDB����
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
		$disp.='<br><small>(�艿 '.GetMoneyString($ITEM[$prn]->{price} * $pr).')</small>';
		}
		else
		{
		$disp.='���� '.GetMoneyString($pr);
		$disp.=    "</a>" if (!$GUEST_USER);
		}
	$disp.=$TD;
	if ($itemno > 0)
		{
		$disp.=GetTagImgItemType($itemno).$ITEM[$itemno]->{name}.' '.$num.$ITEM[$itemno]->{scale};
		$disp.='<br><small>(�艿 '.GetMoneyString($ITEM[$itemno]->{price} * $num).')</small>';
		}
		else
		{
		$disp.='���� '.GetMoneyString($num);
		}
	$disp.=($DT->{id} == $REQ[$i]->{id}) ? $TDB : $TD;
	$disp.=defined($id2idx{$id}) ? ($DT[$id2idx{$id}]->{shopname}) : '�Ȃ�';
	$disp.=defined($id2idx{$mode}) ? "$TD<SPAN>�B��</b></SPAN>" : "$TD ";
	$disp.="$TD����".GetTime2HMS($REQ[$i]->{tm}-$NOW_TIME);
	$enum++ if ($id == $DT->{id});	#�o�i�����J�E���g
	}
$disp.=$TRE.$TBE;
}

