# �A�C�R�����X�g 2004/01/20 �R��

$NOMENU=1;
$Q{bk}="none";
$disp.="<BIG>���A�C�R���ꗗ</BIG><br><br>";

$disp.=$TBT;
foreach my $i(1..$ICON_NUMBER)
	{
	$disp.=$TRT if ($i % 5)==1;
	$disp.='<td width="78">'.$i.GetTagImgKao("",$i)." ";
	$disp.=$TRE if ($i % 5)==0;
	}
$disp.=$TBE;

OutSkin();
1;
