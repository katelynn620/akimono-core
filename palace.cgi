# �{�a 2004/01/20 �R��

RequireFile("inc-palace.cgi");	#�ݒ�t�@�C���ǂݍ���

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

if ($DT->{point} <  $deny_point )
	{
	$disp.='<TABLE cellpadding="26" width="570"><tr>';
	$disp.=qq|<TD style="background-repeat : repeat-x;background-image : url($IMAGE_URL/palace.png);" valign="top"><br><br>|;
	$disp.=$image[1].'����{�a�Ɍ�p�ł����H<b>'.$shopname.'</b>��<b>'.$name.'</b>����B<br>';
	$disp.='�����������É���'.$name.'����Ƃ͖ʉ�ł��Ȃ��Ƃ̋��ł������܂��B';
	$disp.='<br>���������o�c�̎�r�����߂Ă��痈�Ă݂Ă͂ǂ��ł��傤�B'.$TRE;
	$disp.=$TBE."<br>";
	}
	else
	{
	KingMain();
	}

OutSkin();
1;


sub KingMain
{
$disp.='<TABLE cellpadding="26" width="570"><tr>';
$disp.=qq|<TD style="background-repeat : repeat-x;background-image : url($IMAGE_URL/palace.png);" valign="top"><br><br>|;
$disp.=$image[0].'�悭���Q����<b>'.$shopname.'</b>��<b>'.$name.$level.'</b>��B<br>';
$disp.='����͂��˂��˕����y��ł��邼�B�����ł���C���Ȃ���������Ŏg����^����B<br><br>';
$disp.=$msg[$evt].'<br>�����<b>'.GetTagImgItemType($need).$ITEM[$need]->{name}.'��'.$count[$evt].$ITEM[$need]->{scale}.'</b>���߂ĎQ��B';
$disp.='<br>���̎g���������ʂ������Ȃ�΂��Ȃ���'.DignityDefine(1,1).'<b>�݈ʌo���l</b>��^����B����Ă����ȁH'.$TRE;
$disp.=$TBE;

$disp.=<<"HTML";
<br><FORM ACTION="action.cgi" $METHOD>
<INPUT TYPE=HIDDEN NAME=key VALUE="palace-s">
$USERPASSFORM
<BIG>���g���B��</BIG>�F ���l���˗����鏤�i��
<INPUT TYPE=SUBMIT VALUE="�n��"></FORM>
HTML
}