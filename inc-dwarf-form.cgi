# �t�H�[���\�� 2005/03/30 �R��

$disp.=GetMenuTag('dwarf','[��z�փ��X�g]')
	."<b>[��z�ւ��o��]</b>";
$disp.=GetMenuTag('dwarf','[�f�Օi���X�g]','&trade=list') if -e "trade.cgi";
$disp.="<hr width=500 noshade size=1>";

my $cnt=$MAX_BOX - scalar(@SENDWF);
if ($cnt > 0)
{
$preerror="";
LFormCheck() if ($Q{form} eq 'check');
NewLform() if ($preerror || $Q{form} eq 'make');
}
else
{
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>�Z�ݍ��݃h���[�t</SPAN>�F����ȏ�̑�z�ւ��o�����Ƃ͂ł��񂼂��B<br>
�s�K�v�ȑ�z�ւ���������Ȃ肵�Ă��ꂢ�B
$TRE$TBE
HTML
}
1;

sub NewLform
{
FormSet();
$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>�Z�ݍ��݃h���[�t</SPAN>�F���� $cnt��܂ő�z�ւ��o���邼���B<br>
���炤����ɂƂ��Ď���ɂȂ�ʂ悤�ɂȁB
$TRE$TBE<br>$preerror
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
$TB
$TR$TDB<b>����</b>
HTML

$disp.=$TD."<SELECT NAME=to><OPTION VALUE=\"-1\">�|�|����I���|�|";
$disp.="<OPTION VALUE=\"99\">�����̊X�֗A�o��" if -e "trade.cgi";
	foreach (@DT)
	{
		$disp.="<OPTION VALUE=\"$_->{id}\"".($Q{to}==$_->{id} ? ' SELECTED' : '').">$_->{shopname}";
	}
$disp.="</SELECT>\n";
$disp.="<INPUT TYPE=CHECKBOX NAME=notice".(($preerror&&!$Q{notice}) ? '' : ' checked').">";

$disp.=<<"HTML";
�X�ւŒm�点��$TRE
$TR$TDB<b>���i</b>
$TD<SELECT NAME=item SIZE=1>
$formitem
</SELECT> �� <INPUT TYPE=TEXT NAME=num SIZE=7 VALUE="$Q{num}"> ��$TRE
$TR$TDB<b>���</b>
$TD<INPUT TYPE=TEXT NAME=price SIZE=12 VALUE="$Q{price}"> $term[2](
<INPUT TYPE=CHECKBOX NAME=unit>�P���w��)
$TR$TD<SPAN>�g�p�@</SPAN>$TD
�E���i�𑊎�ɑ���C���̑�����Ƃ邱�Ƃ��ł��܂��B<br>
�E��z�ւ𑗂������Ƃ������I�Ɂu�X�ւŒm�点��v���Ƃ��ł��܂��B<br>
�E�萔���Ƃ��đ���� <b>$DTTaxrate%</b>�̐ŋ���������܂��B
$TBE
<br><INPUT TYPE=HIDDEN NAME=form VALUE="check">
<INPUT TYPE=SUBMIT VALUE="���M�m�F">
</FORM>
HTML
}

sub LFormCheck
{
my $to=$Q{to};
my $toname;
$preerror="������w�肵�Ă��������B", return if $to==-1;
OutError("�������g�ɑ�z�ւ��o�����Ƃ͂ł��܂���B") if ($to == $DT->{id});
if ($to==99)
	{
	$preerror="�f�Ղ��Ȃ����Ă��Ȃ��̂Ŏw��ł��܂���B", return unless -e "trade.cgi";
	$toname="���̊X�֗A�o";
	$Q{notice}=0;
	}
	else
	{
	$preerror="���݂��Ȃ��X�܂ł��B", return if !defined($id2idx{$to});
	$toname=$DT[$id2idx{$to}]->{shopname};
	}
$preerror="�A�C�e���̎w�肪�s���ł��B", return if !$ITEM[$Q{item}]->{name};
$preerror="�A�C�e���̎w�肪�s���ł��B", return if $ITEM[$Q{item}]->{flag}=~/r/;	# r �˗��s��

$Q{num}||=$DT->{item}[$Q{item}-1];
$Q{num}=CheckCount($Q{num},0,0,$DT->{item}[$Q{item}-1]);
$preerror="�A�C�e���̍݌ɂ�����܂���B", return if !$Q{num};
my $price=CheckCount($Q{price},0,0,$MAX_MONEY);
$price=$price * $Q{num} if $Q{unit};
$preerror="������w�肵�Ă��������B", return if !$price;
my $numrate=$ITEM[$Q{item}]->{price} * $Q{num};
$preerror="���i�̉��l�Ƒ�����肠���Ă��܂���B", return if ($price > $numrate * 2) || ($numrate > $price * 2);
my $pricestring=GetMoneyString($price);

$disp.=<<"HTML";
$TB$TR
$TD$image[0]$TD
<SPAN>�Z�ݍ��݃h���[�t</SPAN>�F���̓��e�ő�z�ւ��o�������B<br>
����Ŗ��Ȃ����m�F���Ă��ꂢ�B
$TRE$TBE<br>
$TB$TR$TD
<SPAN>����</SPAN>�F$toname<br>
<SPAN>���i</SPAN>�F$ITEM[$Q{item}]->{name} �~ $Q{num} $ITEM[$Q{item}]->{scale}<br>
<SPAN>���</SPAN>�F$pricestring
$TRE$TBE
<FORM ACTION="action.cgi" $METHOD>
$MYFORM$USERPASSFORM
<INPUT TYPE=HIDDEN NAME=to VALUE="$to">
<INPUT TYPE=HIDDEN NAME=notice VALUE="$Q{notice}">
<INPUT TYPE=HIDDEN NAME=item VALUE="$Q{item}">
<INPUT TYPE=HIDDEN NAME=num VALUE="$Q{num}">
<INPUT TYPE=HIDDEN NAME=price VALUE="$Q{price}">
<INPUT TYPE=HIDDEN NAME=unit VALUE="$Q{unit}">
<INPUT TYPE=HIDDEN NAME=form VALUE="make">
<INPUT TYPE=SUBMIT NAME=ok VALUE="���M">
<INPUT TYPE=SUBMIT NAME=ng VALUE="�ĕҏW">
</FORM>
HTML
}

sub FormSet
{
	my @sort;
	foreach(1..$MAX_ITEM){$sort[$_]=$ITEM[$_]->{sort}};
	my @itemlist=sort { $sort[$a] <=> $sort[$b] } (1..$MAX_ITEM);
	$formitem="";
	foreach my $idx (@itemlist)
	{
		next if !$ITEM[$idx]->{name};
		next if $ITEM[$idx]->{flag}=~/r/;	# r �˗��s��
		my $cnt=$DT->{item}[$idx-1];
		my $scale=$ITEM[$idx]->{scale};
		my $price=$ITEM[$idx]->{price};
		$formitem.="<OPTION VALUE=\"$idx\"".($Q{item}==$idx ? ' SELECTED' : '').">$ITEM[$idx]->{name}($cnt$scale@".GetMoneyString($price).")" if $cnt;
	}
}


