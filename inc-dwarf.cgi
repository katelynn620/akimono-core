# ��z�փ��X�g�\�� 2005/01/06 �R��

$disp.="<b>[��z�փ��X�g]</b> "
	.GetMenuTag('dwarf',		'[��z�ւ��o��]','&form=make');
$disp.=GetMenuTag('dwarf','[�f�Օi���X�g]','&trade=list') if -e "trade.cgi";
$disp.="<hr width=500 noshade size=1>";

if (!$NeverD)
	{
	$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>�Z�ݍ��݃h���[�t</SPAN>�F�h���[�t��z�ւ͗R������g�D����B<br>
���V�ɗ���ł����΁C���ł����i�𑗂�͂��邼���B
$TRE$TBE<br>
HTML
	}
	else
	{
	$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>�Z�ݍ��݃h���[�t</SPAN>�F�V���� $NeverD��̑�z�ւ��͂��Ă��邼�B<br>
�󂯎�邩�C����Ƃ��f�邩���߂Ă��ꂢ�B
$TRE$TBE<br>
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="plus">
HTML
	}
DwarfReading() if scalar(@RECDWF);
DwarfSending() if scalar(@SENDWF);
1;


sub DwarfReading
{
	$disp.=<<"HTML";
<BIG>���͂�����z��</BIG><br><br>
$TB$TR
$TD�^
$TDB���t�i
$TDB���
$TDB���t��
$TDB���
$TDB����
$TRE
HTML

my @MODE;
$MODE[0]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign4.png">�A���\\��|;
$MODE[1]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign1.png">�V��|;
$MODE[2]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign2.png">���ς�|;
$MODE[3]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign3.png">��拑��|;
$MODE[4]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign2.png">�A���ς�|;
$MODE[5]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign3.png">�A�����s|;

foreach my $i(@RECDWF)
	{
	my($no,$from,$item,$num,$price,$mode)=($DWF[$i]->{no},$DWF[$i]->{from},$DWF[$i]->{item},$DWF[$i]->{num},$DWF[$i]->{price},$DWF[$i]->{mode});
	$disp.=$TR.$TD;
	$disp.=($mode==1) ? "<input type=checkbox name=\"act_".$DWF[$i]->{no}."\" value=\"1\">" : " ";
	$disp.=$TD.GetTagImgItemType($item).$ITEM[$item]->{name}.' '.$num.$ITEM[$item]->{scale};
	$disp.='<br><small>(�艿 '.GetMoneyString($ITEM[$item]->{price} * $num).')</small>';
	$disp.=$TD.GetMoneyString($price).$TD;
	if ($from==99)
		{
		$disp.='���̊X';
		$mode+=2 if $mode>1;
		}
		else
		{
		$disp.=defined($id2idx{$from}) ? ($DT[$id2idx{$from}]->{shopname}) : '�Ȃ�';
		}
	$disp.=$TD.$MODE[$mode].$TD;
	$disp.=($DWF[$i]->{trade} eq "") ? "����".GetTime2HMS($DWF[$i]->{tm}-$NOW_TIME+$BOX_STOCK_TIME) : "�|�|�|�|�|�|";
	$disp.=$TRE;


	}
$disp.=$TBE."<br>";
$disp.=<<"HTML" if ($NeverD);
�I��������z�ւɂ��� <INPUT TYPE=SUBMIT NAME=ok VALUE="����𕥂��Ď󂯎��">
<INPUT TYPE=SUBMIT NAME=ng VALUE="�󂯎���f��">
</FORM><br>
HTML
}

sub DwarfSending
{
	$disp.=<<"HTML";
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=mode VALUE="delete">
<BIG>����������z��</BIG><br><br>
$TB$TR
$TD�^
$TDB���t�i
$TDB���
$TDB���t��
$TDB���
$TDB����
$TRE
HTML

my @MODE;
$MODE[0]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign4.png">�A�o�҂�|;
$MODE[1]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign4.png">���҂�|;
$MODE[2]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign2.png">���ς�|;
$MODE[3]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign3.png">��拑��|;
$MODE[4]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign2.png">�A�o����|;
$MODE[5]=qq|<IMG class="i" SRC="$IMAGE_URL/map/dwfsign3.png">�A�o���s|;

my $tradeonly=1;
foreach my $i(@SENDWF)
	{
	my($no,$to,$item,$num,$price,$mode)=($DWF[$i]->{no},$DWF[$i]->{to},$DWF[$i]->{item},$DWF[$i]->{num},$DWF[$i]->{price},$DWF[$i]->{mode});
	$disp.=$TR.$TD;
	$disp.="<input type=checkbox name=\"del_".$DWF[$i]->{no}."\" value=\"1\">" if ($to!=99);
	$disp.=$TD.GetTagImgItemType($item).$ITEM[$item]->{name}.' '.$num.$ITEM[$item]->{scale};
	$disp.='<br><small>(�艿 '.GetMoneyString($ITEM[$item]->{price} * $num).')</small>';
	$disp.=$TD.GetMoneyString($price).$TD;
	if ($to==99)
		{
		$disp.='���̊X';
		$mode=0 if $mode==1;
		$mode+=2 if $mode>1;
		}
		else
		{
		$tradeonly=0;
		$disp.=defined($id2idx{$to}) ? ($DT[$id2idx{$to}]->{shopname}) : '�Ȃ�';
		}
	$disp.=$TD.$MODE[$mode].$TD;
	$disp.=($DWF[$i]->{trade} eq "") ? "����".GetTime2HMS($DWF[$i]->{tm}-$NOW_TIME+$BOX_STOCK_TIME) : "�|�|�|�|�|�|";
	$disp.=$TRE;
	}
$disp.=$TBE."<br>";
$disp.=<<"HTML" if !$tradeonly;
�I��������z�ւ� <INPUT TYPE=SUBMIT VALUE="�폜����">
</FORM>
HTML
}

