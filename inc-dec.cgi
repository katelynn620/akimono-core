# ����f�R�[�h 2003/09/25 �R��

OutError("���M�T�C�Y���傫�����܂�") if ($ENV{'CONTENT_LENGTH'} > 10240);
require $JCODE_FILE;

binmode(STDIN);
my $Boundary = <STDIN>;
$Boundary =~ s/\x0D\x0A//;
while (<STDIN>) {
	if (/^\s*Content-Disposition:/i) {
		my $Name;
		# �t�H�[���̍��ږ��𓾂�
		if (/\bname="([^"]+)"/i or /\bname=([^\s:;]+)/i) {
			$Name = $1;
		}
		# �t�@�C�������擾
		if (/\bfilename="([^"]*)"/i or /\bfilename=([^\s:;]*)/i) {
			$FILENAME{$Name} = $1 || 'unknown';
		}
		# �w�b�_���e��ǂݎ��
		# �w�b�_�̏I����������s�����o�����烋�[�v�𔲂���
		while (<STDIN>) {
			last if (not /\w/);
			if (
				/^\s*Content-Type:\s*"([^"]+)"/i
				or /^\s*Content-Type:\s*([^\s:;]+)/i
			) {
			$MIMETYPE{$Name} = $1;
			}
		}
		# �f�[�^�{�̂�ǂݎ��
		# �f�[�^�̏I��������Boundary�����o�����烋�[�v�𔲂���
		while (<STDIN>) {
			last if (/^\Q$Boundary\E/);
			$Q{$Name} .= $_;
		}
		$Q{$Name} =~s /\x0D\x0A$//; # ������\r\n����菜��
		if ($Q{$Name}) {
			# �t�@�C���̏ꍇ
			if ($FILENAME{$Name} or $MIMETYPE{$Name}) {
				# MacBinary�����o���č폜
				if (
					$MIMETYPE{$Name}
					=~ /^application\/(x-)?macbinary$/i
				) {
				# Header�Ɩ����̃��\�[�X���폜
					$Q{$Name} = substr(
						$Q{$Name},
						128,
						unpack("N", substr($Q{$Name}, 83, 4))
					);
				}
			}
			# �t�@�C���ȊO�̏ꍇ
			else {
				&jcode::convert(\$Q{$Name}, 'sjis');
				$Q{$Name} =~ s/&/&amp;/g;
				$Q{$Name} =~ s/"/&quot;/g;
				$Q{$Name} =~ s/</&lt;/g;
				$Q{$Name} =~ s/>/&gt;/g;
				$Q{$Name} =~ s/\x0D\x0A/<br>/g;
				$Q{$Name} =~ s/\x0D/<br>/g;
				$Q{$Name} =~ s/\x0A/<br>/g;
			}
		}
	}
	# Boundary�����o�����烋�[�v�𔲂���
	last if (/^\Q$Boundary--\E/);
}
	@Q{qw(nm pw ss)}=split(/!/,$Q{u},3) if exists $Q{u};
1;
