# ���z���Z���^�[ 2004/01/20 �R��

OutError('�ړ]���s�ɐݒ肳��Ă��܂�') if !$MOVETOWN_ENABLE;
OutError('�X�R�[�h���ݒ肳��Ă��܂���') if !$TOWN_CODE;
my $townmaster=ReadTown($TOWN_CODE,'getown');
OutError('�ړ]���[�g���Ȃ����Ă��܂���') if !$townmaster;

DataRead();
CheckUserPass();

$disp.=GetTownListHTML();
OutSkin();
1;


sub GetTownListHTML
{
	my @townlist=ReadTown();
	return '<b>�ړ]�\�ȊX��������܂���</b>' if !scalar(@townlist);
	
	my $ret;
	$ret.='<BIG>�����̊X�ֈ��z��</BIG><br><br>';
	$ret.=$TBT.$TRT.$TD;
	foreach(@townlist)
	{
		$ret.="<SPAN>".$_->{name}."</SPAN><br>";
		$ret.=GetTagA("[�m�F]","action.cgi?key=jump&town=$_->{code}",0,"_blank");
		$ret.=GetTagA("[�ړ]�葱]","action.cgi?key=move-f&$USERPASSURL&towncode=$_->{code}") if !$GUEST_USER;
		$ret.="<br>".$_->{comment}."<br><br>";
	}
	$ret.=$TRE.$TBE;
	return $ret;
}

