# �A�C�e�����X�g 2005/03/30 �R��

# -------- �ݒ蕔�� ---------
# �{���ݒ�
$listcheck=2;		# �A�C�e���Љ��0:�X�܏��L�҂�������Ȃ��C 1:�N�ł������C 2:�Ǘ��҂�������Ȃ��i�����j�B

# �v���C���[�ɂ͌����Ȃ��A�C�e���i�ԍ��Ŏw��j
# �w���c $DENYITEM='25,86';  ��No.25��86��\�����Ȃ��B

$DENYITEM='';

# �v���C���[������Ƃ��̕\���ݒ�
$design_no=0;		#�A�C�e���m����0:�\�����Ȃ��i�����j�C 1:�\������B
$design_sale=0;		#����s����0:�\�����Ȃ��i�����j�C 1:�\������B
$design_prof=1;		#���v����0:���l�ŕ\���C 1:�T�i�K�\���i�����j�B
$design_rank=1;		#�l�C����0:���l�ŕ\���C 1:�T�i�K�\���i�����j�B
$design_plus=1;		#�s����ׂ�0:���l�ŕ\���C 1:���~�ŕ\���i�����j�B

# -------- �ݒ芮�� ---------

DataRead();
CheckUserPass($listcheck);
$DENYITEM=','.$DENYITEM.',';

if ($MASTER_USER) {
$NOMENU=1;
$Q{bk}="none";
@NGItem=(0);
$design_no=1;
$design_sale=1;
$design_prof=0;
$design_rank=0;
$design_plus=0;
$disp.="<BIG>���A�C�e���f�[�^</BIG><br><br>";
} else {
OutError("bad request") if ($listcheck == 2);
$disp.="<BIG>���A�C�e���Љ�</BIG><br><br>";
}

my $tp=int($Q{tp}+0);
undef %adminitemlist;
my($ITEM,$stock,$price,$mpl,$mph,$popular,$uppoint);

foreach my $no(1..$MAX_ITEM)
{
	next if ($DENYITEM =~ /,$no,/);
	$ITEM=$ITEM[$no];
	next if ($ITEM->{type} != $tp)&&($tp != 0);;
	$adminitemlist{$no}=$ITEM;
}

foreach my $cnt (0..$#ITEMTYPE)
{
	$disp.=$cnt==$tp ? "[" : "<A HREF=\"action.cgi?key=item-list&$USERPASSURL&tp=$cnt\">";
	$disp.=GetTagImgItemType(0,$cnt) if $cnt && !$MOBILE;
	$disp.=$ITEMTYPE[$cnt];
	$disp.=$cnt==$tp ? "]" :"</A>";
	$disp.=" ";
}
	$disp.="<br>";

my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{pg},$LIST_PAGE_ROWS,scalar(keys(%adminitemlist)));

$disp.=GetPageControl($pageprev,$pagenext,"tp=$tp","",$pagemax,$page);

$disp.=$TB;
$disp.=$TR;
$disp.=$TDB.'No.' if $design_no;
$disp.=$TDB.'���i��';
$disp.=$TDB.'�W�����i';
$disp.=$TDB.'�ێ���';
$disp.=$TDB.'���s' if $design_sale;
$disp.=$TDB.'���v��';
$disp.=$TDB.'�l�C��';
$disp.=$TDB.'����';
$disp.=$TDB.'����';
$disp.=$TRE;
foreach my $ITEM ((sort{$a->{sort} <=> $b->{sort}} values(%adminitemlist))[$pagestart..$pageend])
{
	my $itemno=$ITEM->{no};
	$disp.=$TR;
	$disp.=$TDNW.$itemno if $design_no;
	$disp.=$TDNW;
	$disp.=GetTagImgItemType($itemno).$ITEM->{name}."</A>";
	$disp.=$TDNW.GetMoneyString($ITEM->{price});
	$disp.=$TDNW.GetMoneyString($ITEM->{cost});

	my $admin_item=int($ITEM->{popular}/$SALE_SPEED);

	$disp.=$TDNW.($admin_item ? GetTime2HMS($admin_item) : "�~")  if $design_sale;

	if ($design_prof) {
	$disp.=$TDNW.($admin_item ? GetStarRank(int($ITEM->{price} *24*6*6/10 / $admin_item)) : "");
	} else {
	$disp.=$TDNW.($admin_item ? int($ITEM->{price} *24*6*6/10 / $admin_item) : "---");
	}

	if ($design_rank) {
	$disp.=$TDNW.($admin_item ? GetStarRank(int($ITEM->{point} *24*6*6/10 / $admin_item)) : "");
	} else {
	$disp.=$TDNW.($admin_item ? int($ITEM->{point} *24*6*6/10 / $admin_item) : "---");
	}

	if ($ITEM->{plus} > 0) { 
	$disp.=($design_plus ? $TDNW."��" : $TDNW.GetTime2HMS($ITEM->{plus}));
	} else { $disp.=$TDNW."�~" }

	$disp.=$TDNW."<small>".$ITEM->{info}."</small>";
	$disp.=$TRE;
}
$disp.=$TBE;
$disp.=GetPageControl($pageprev,$pagenext,"tp=$tp","",$pagemax,$page);
OutSkin();
1;

sub GetStarRank		#�\���̃J�X�^�}�C�Y�\�B
{
	my($no)=@_;
	my $flag='<font color="#cccc99">||</font>';
	$flag.='<font color="#ddcc44">||</font>' if $no > 50;
	$flag.='<font color="#ffcc00">||</font>' if $no > 90;
	$flag.='<font color="#ff9900">||</font>' if $no > 120;
	$flag.='<font color="#ff6600">||</font>' if $no > 180;
	return $flag;
}
