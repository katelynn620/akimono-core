# �{�a�B������ 2004/01/20 �R��

Lock();
RequireFile("inc-palace.cgi");
$image[0]=GetTagImgKao("���l","king",'align="left" ');
$image[1]=GetTagImgKao("��b","minister",'align="left" ');

DataRead();
CheckUserPass();

$evt=GetTownData('evt');
$evt=0 if (!$evt);
$level=DignityDefine($DT->{dignity});

$disp.="<BIG>���{�a</BIG><br><br>";

$shopname=$DT->{shopname};
$name=$DT->{name};
$need=$itemno[$evt];

if ( $DT->{item}[$need-1] < $count[$evt] )
	{
	$disp.='<TABLE cellpadding="26" width="570"><tr>';
	$disp.=qq|<TD style="background-repeat : repeat-x;background-image : url($IMAGE_URL/palace.png);" valign="top"><br><br>|;
	$disp.=$image[0].'�������Ƃ������Ƃ�<b>'.$shopname.'</b>��<b>'.$name.$level.'</b>��B<br>';
	$disp.='<b>'.GetTagImgItemType($need).$ITEM[$need]->{name}.$count[$evt].$ITEM[$need]->{scale}.'</b>�́C���܂������Ă��Ȃ��ł͂Ȃ����I<br>';
	$disp.='����Ƃ�'.$name.'�͗]�����炩���Ă���̂ł͂���܂��ȁH';
	$disp.='<br>�͂₭�g����B������̂���B��߂�ߖY���łȂ����B'.$TRE;
	$disp.=$TBE."<br>���l�͂Ղ�Ղ�{��o���Ă��܂��܂����B";
	}
	else
	{
	$disp.='<TABLE cellpadding="26" width="570"><tr>';
	$disp.=qq|<TD style="background-repeat : repeat-x;background-image : url($IMAGE_URL/palace.png);" valign="top"><br><br>|;
	$disp.=$image[0].'�����ςꂶ��<b>'.$shopname.'</b>��<b>'.$name.$level.'</b>��B<br>';
	$disp.='<b>'.GetTagImgItemType($need).$ITEM[$need]->{name}.$count[$evt].$ITEM[$need]->{scale}.'</b>�͊m���Ɏ󂯎�������B<br>';
	$disp.='����Ă��Ȃ��ɖJ���Ƃ���'.DignityDefine(1,1).'<b>�݈ʌo���l</b>��^���悤�B'.$TRE;
	$disp.=$TBE."<br>";

	$DT->{item}[$need-1] -= $count[$evt];
	$DT->{dignity}++;
	$evt=int(rand(scalar(@itemno)));
	SetTownData('evt',$evt);

	PushLog(0,0,$DT->{shopname}.'�����l�̎g����B�����܂����B');
	RenewLog();
	DataWrite();
	DataCommitOrAbort();
	}
UnLock();
OutSkin();
1;
