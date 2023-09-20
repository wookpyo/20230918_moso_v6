from django.db import models

MACHINE_NUMBER = (
    ('','Injection 기계 선택'),
    ('1호기','1호기'),
    ('2호기','2호기'),
    ('3호기','3호기'),
    ('4호기','4호기'),
)

class Injection(models.Model):

    #/- 기계정보
    machine_number = models.CharField(max_length=50, null=True, choices=MACHINE_NUMBER) # 기계 호기 ok

    #/- 생산 인원
    male_1 = models.CharField(max_length=20) # 남성 1 ok
    male_2 = models.CharField(max_length=20) # 남성 2 ok
    male_3 = models.CharField(max_length=20) # 남성 3 ok
    female_1 = models.CharField(max_length=20) # 여성 1 ok
    female_2 = models.CharField(max_length=20) # 여성 2 ok
    female_3 = models.CharField(max_length=20) # 여성 3 ok
    female_4 = models.CharField(max_length=20) # 여성 4 ok
    female_5 = models.CharField(max_length=20) # 여성 5 ok
    female_6 = models.CharField(max_length=20) # 여성 6 ok

    #/- 발주
    product_name = models.CharField(max_length=50) # 제품명 ok
    product_color = models.CharField(max_length=50,null=True) # 제품 컬러
    order_number = models.CharField(max_length=50) # 발주 번호 
    order_quantity = models.CharField(max_length=50) # 발주 수량

    #/- 생산
    work_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="작업일") # 작업일
    work_time = models.CharField(max_length=50) # 시간표기
    work_team = models.CharField(max_length=50) # 주간/야간

    quantity = models.CharField(max_length=50) # 생산 수량
    quantity_per_box = models.CharField(max_length=50) # 박스당 개입수
    box_quantity = models.CharField(max_length=50) # 총 박스 수량

    cycle_time = models.CharField(max_length=20) # 싸이클타임
    cavity_weight = models.CharField(max_length=50) # 캐비티 무게
    cavity_quantity = models.CharField(max_length=50) # 캐비티 갯수
    resin = models.CharField(max_length=50) # 원료
    masterbatch_number = models.CharField(max_length=50) # 마스터뱃치 넘버
    
    chiller_temperature = models.CharField(max_length=50) # 칠러 온도
    hopper_temperature = models.CharField(max_length=50) # 호퍼 온도
    hot_oil_temperature = models.CharField(max_length=50) # 온유기 온도
    masterbatch_dry_temperature = models.CharField(max_length=50) # 마스터뱃치 건조 온도

    bottom_option = models.CharField(max_length=50) # 보톰 옵션

    time_injection1 = models.CharField(max_length=20) # 타이머설정(사출) - 사출 시간
    time_injection2 = models.CharField(max_length=20) # 타이머설정(사출) - 냉각 시간
    time_injection3 = models.CharField(max_length=20) # 타이머설정(사출) - 사출 시작
    time_injection4 = models.CharField(max_length=20) # 타이머설정(사출) - 스크류 장전 시작
    time_injection5 = models.CharField(max_length=20) # 타이머설정(사출) - 스크류 감압 시간
    time_injection6 = models.CharField(max_length=20) # 타이머설정(사출) - 핫 러너 차단 폐쇄
    time_injection7 = models.CharField(max_length=20) # 타이머설정(사출) - HR 밸브 주입구 핀 개방 시작
    time_injection8 = models.CharField(max_length=20) # 타이머설정(사출) - 차단 노즐 폐쇄 시작
    time_injection9 = models.CharField(max_length=20) # 타이머설정(사출) - 사출코어금형 에어 분사 시간

    time_injection10 = models.CharField(max_length=20) # 타이머설정(가열) - 가열 코어 하강 시작
    time_injection11 = models.CharField(max_length=20) # 타이머설정(가열) - 가열 코어 하강 시간
    time_injection12 = models.CharField(max_length=20) # 타이머설정(가열) - 가열 포트 상승 시작
    time_injection13 = models.CharField(max_length=20) # 타이머설정(가열) - 가열 포트 상승 시간
    time_injection14 = models.CharField(max_length=20) # 타이머설정(가열) - 온조 블로우 시작
    time_injection15 = models.CharField(max_length=20) # 타이머설정(가열)- 온조 블로우 시간
    time_injection16 = models.CharField(max_length=20) # 타이머설정(가열) - 온조 블로우 감압
    time_injection17 = models.CharField(max_length=20) # 타이머설정(가열) - 온조부냉각 블로 개시
    time_injection18 = models.CharField(max_length=20) # 타이머설정(가열) - 조건부 냉각 블로우 시간
    time_injection19 = models.CharField(max_length=20) # 타이머설정(가열) - 조건부 냉각 블로우 감압 시간

    time_injection20 = models.CharField(max_length=20) # 타이머설정(블로우) - 블로우 시간
    time_injection21 = models.CharField(max_length=20) # 타이머설정(블로우) - 블로우 감압 시간
    time_injection22 = models.CharField(max_length=20) # 타이머설정(블로우) - 1차 블로우 시간
    time_injection23 = models.CharField(max_length=20) # 타이머설정(블로우) - 2차 블로우 시간
    time_injection24 = models.CharField(max_length=20) # 타이머설정(블로우) - 블로우 에어 복구
    time_injection25 = models.CharField(max_length=20) # 타이머설정(블로우) - 냉각 블로우 시간
    time_injection26 = models.CharField(max_length=20) # 타이머설정(블로우) - 스트레치 하강 시작
    time_injection27 = models.CharField(max_length=20) # 타이머설정(블로우) - 스트레치 시간
    time_injection28 = models.CharField(max_length=20) # 타이머설정(블로우) - 보톰 금형(지연)시작

    heating_setting1 = models.CharField(max_length=20) # 온도설정(배럴) - 노즐
    heating_setting2 = models.CharField(max_length=20) # 온도설정(배럴) - 전면
    heating_setting3 = models.CharField(max_length=20) # 온도설정(배럴) - 가운데
    heating_setting4 = models.CharField(max_length=20) # 온도설정(배럴) - 후면F
    heating_setting5 = models.CharField(max_length=20) # 온도설정(배럴) - 후면R

    heating_setting6 = models.CharField(max_length=20) # 온도설정(HR노즐) - 1
    heating_setting7 = models.CharField(max_length=20) # 온도설정(HR노즐) - 2
    heating_setting8 = models.CharField(max_length=20) # 온도설정(HR노즐) - 3
    heating_setting9 = models.CharField(max_length=20) # 온도설정(HR노즐) - 4
    heating_setting10 = models.CharField(max_length=20) # 온도설정(HR노즐) - 5
    heating_setting11 = models.CharField(max_length=20) # 온도설정(HR노즐) - 6
    heating_setting12 = models.CharField(max_length=20) # 온도설정(HR노즐) - 7
    heating_setting13 = models.CharField(max_length=20) # 온도설정(HR노즐) - 8
    heating_setting14 = models.CharField(max_length=20) # 온도설정(HR노즐) - 9
    heating_setting15 = models.CharField(max_length=20) # 온도설정(HR노즐) - 10
    heating_setting16 = models.CharField(max_length=20) # 온도설정(HR노즐) - 11
    heating_setting17 = models.CharField(max_length=20) # 온도설정(HR노즐) - 12

    heating_setting18 = models.CharField(max_length=20) # 온도설정(HR블록) - 1
    heating_setting19 = models.CharField(max_length=20) # 온도설정(HR블록) - 2
    heating_setting20 = models.CharField(max_length=20) # 온도설정(HR블록) - 3
    heating_setting21 = models.CharField(max_length=20) # 온도설정(HR블록) - 4
    heating_setting22 = models.CharField(max_length=20) # 온도설정(HR블록) - 5
    heating_setting23 = models.CharField(max_length=20) # 온도설정(HR블록) - 6
    heating_setting24 = models.CharField(max_length=20) # 온도설정(HR블록) - 7
    heating_setting25 = models.CharField(max_length=20) # 온도설정(HR블록) - 8
    heating_setting26 = models.CharField(max_length=20) # 온도설정(HR블록) - 스프루

    heating_setting27 = models.CharField(max_length=20) # 온도설정(가열 코어) - 1
    heating_setting28 = models.CharField(max_length=20) # 온도설정(가열 코어) - 2
    heating_setting29 = models.CharField(max_length=20) # 온도설정(가열 코어) - 3
    heating_setting30 = models.CharField(max_length=20) # 온도설정(가열 코어) - 4
    heating_setting31 = models.CharField(max_length=20) # 온도설정(가열 코어) - 5
    heating_setting32 = models.CharField(max_length=20) # 온도설정(가열 코어) - 6
    heating_setting33 = models.CharField(max_length=20) # 온도설정(가열 코어) - 7
    heating_setting34 = models.CharField(max_length=20) # 온도설정(가열 코어) - 8
    heating_setting35 = models.CharField(max_length=20) # 온도설정(가열 코어) - 9
    heating_setting36 = models.CharField(max_length=20) # 온도설정(가열 코어) - 10
    heating_setting37 = models.CharField(max_length=20) # 온도설정(가열 코어) - 11
    heating_setting38 = models.CharField(max_length=20) # 온도설정(가열 코어) - 12

    heating_setting39 = models.CharField(max_length=20) # 온도설정(가열 포트 L) - 1
    heating_setting40 = models.CharField(max_length=20) # 온도설정(가열 포트 L) - 2
    heating_setting41 = models.CharField(max_length=20) # 온도설정(가열 포트 L) - 3
    heating_setting42 = models.CharField(max_length=20) # 온도설정(가열 포트 L) - 4
    heating_setting43 = models.CharField(max_length=20) # 온도설정(가열 포트 L) - 5
    heating_setting44 = models.CharField(max_length=20) # 온도설정(가열 포트 L) - 6
    heating_setting45 = models.CharField(max_length=20) # 온도설정(가열 포트 L) - 7
    heating_setting46 = models.CharField(max_length=20) # 온도설정(가열 포트 L) - 8
    heating_setting47 = models.CharField(max_length=20) # 온도설정(가열 포트 L) - 9
    heating_setting48 = models.CharField(max_length=20) # 온도설정(가열 포트 L) - 10
    heating_setting49 = models.CharField(max_length=20) # 온도설정(가열 포트 L) - 11
    heating_setting50 = models.CharField(max_length=20) # 온도설정(가열 포트 L) - 12

    heating_setting51 = models.CharField(max_length=20) # 온도설정(가열 포트 R) - 1
    heating_setting52 = models.CharField(max_length=20) # 온도설정(가열 포트 R) - 2
    heating_setting53 = models.CharField(max_length=20) # 온도설정(가열 포트 R) - 3
    heating_setting54 = models.CharField(max_length=20) # 온도설정(가열 포트 R) - 4
    heating_setting55 = models.CharField(max_length=20) # 온도설정(가열 포트 R) - 5
    heating_setting56 = models.CharField(max_length=20) # 온도설정(가열 포트 R) - 6
    heating_setting57 = models.CharField(max_length=20) # 온도설정(가열 포트 R) - 7
    heating_setting58 = models.CharField(max_length=20) # 온도설정(가열 포트 R) - 8
    heating_setting59 = models.CharField(max_length=20) # 온도설정(가열 포트 R) - 9
    heating_setting60 = models.CharField(max_length=20) # 온도설정(가열 포트 R) - 10
    heating_setting61 = models.CharField(max_length=20) # 온도설정(가열 포트 R) - 11
    heating_setting62 = models.CharField(max_length=20) # 온도설정(가열 포트 R) - 12

    injetion_setting1 = models.CharField(max_length=20) # 사출 제어 (위치 mm) - M2
    injetion_setting2 = models.CharField(max_length=20) # 사출 제어 (위치 mm) - M1
    injetion_setting3 = models.CharField(max_length=20) # 사출 제어 (위치 mm) - P-V
    injetion_setting4 = models.CharField(max_length=20) # 사출 제어 (위치 mm) - 3-2
    injetion_setting5 = models.CharField(max_length=20) # 사출 제어 (위치 mm) - 2-1
    injetion_setting6 = models.CharField(max_length=20) # 사출 제어 (위치 mm) - 사출 크기
    injetion_setting7 = models.CharField(max_length=20) # 사출 제어 (압력 MPa) - 5
    injetion_setting8 = models.CharField(max_length=20) # 사출 제어 (압력 MPa) - 4
    injetion_setting9 = models.CharField(max_length=20) # 사출 제어 (압력 MPa) - 3
    injetion_setting10 = models.CharField(max_length=20) # 사출 제어 (압력 MPa) - 2
    injetion_setting11 = models.CharField(max_length=20) # 사출 제어 (압력 MPa) - 1
    injetion_setting12 = models.CharField(max_length=20) # 사출 제어 (속도 %) - 5
    injetion_setting13 = models.CharField(max_length=20) # 사출 제어 (속도 %) - 4
    injetion_setting14 = models.CharField(max_length=20) # 사출 제어 (속도 %) - 3
    injetion_setting15 = models.CharField(max_length=20) # 사출 제어 (속도 %) - 2
    injetion_setting16 = models.CharField(max_length=20) # 사출 제어 (속도 %) - 1
    injetion_setting17 = models.CharField(max_length=20) # 사출 제어 (사출 시간)
    injetion_setting18 = models.CharField(max_length=20) # 사출 제어 (냉각 시간)
    injetion_setting19 = models.CharField(max_length=20) # 사출 제어 (사출 시작)

    injetion_setting19 = models.CharField(max_length=20) # 스크류 회전 (흘림 방지 초)
    injetion_setting20 = models.CharField(max_length=20) # 스크류 회전 (위치 PN1)
    injetion_setting21 = models.CharField(max_length=20) # 스크류 회전 (사출 크기)
    injetion_setting22 = models.CharField(max_length=20) # 스크류 회전 (압력 MPa) - 흘림 방지
    injetion_setting23 = models.CharField(max_length=20) # 스크류 회전 (압력 MPa) - 1
    injetion_setting24 = models.CharField(max_length=20) # 스크류 회전 (압력 MPa) - 2
    injetion_setting25 = models.CharField(max_length=20) # 스크류 회전 (속도 %) - 흘림 방지
    injetion_setting26 = models.CharField(max_length=20) # 스크류 회전 (속도 %) - 1
    injetion_setting27 = models.CharField(max_length=20) # 스크류 회전 (속도 %) - 2
    injetion_setting28 = models.CharField(max_length=20) # 스크류 회전 - 스크류 감압 시간
    injetion_setting29 = models.CharField(max_length=20) # 스크류 회전 - 스크류 장전 시작
    injetion_setting30 = models.CharField(max_length=20) # 스크류 회전 - 스크류 속도 상승

    injetion_setting31 = models.CharField(max_length=20) # 퍼지 펌프 설정(스크류 후진) - 압력 MPa
    injetion_setting32 = models.CharField(max_length=20) # 퍼지 펌프 설정(스크류 후진) - 속도 %
    injetion_setting33 = models.CharField(max_length=20) # 퍼지 펌프 설정(사출장치 전진) - 압력 MPa
    injetion_setting34 = models.CharField(max_length=20) # 퍼지 펌프 설정(사출장치 전진) - 속도 %
    injetion_setting35 = models.CharField(max_length=20) # 퍼지 펌프 설정(사출장치 후진) - 압력 MPa
    injetion_setting36 = models.CharField(max_length=20) # 퍼지 펌프 설정(사출장치 후진) - 속도 %
    injetion_setting37 = models.CharField(max_length=20) # 퍼지 펌프 설정(언로드) - 압력 MPa
    injetion_setting38 = models.CharField(max_length=20) # 퍼지 펌프 설정(언로드) - 속도 %
    injetion_setting39 = models.CharField(max_length=20) # 퍼지 경보 설정(과보압)
    injetion_setting40 = models.CharField(max_length=20) # 퍼지 경보 설정(미성형)
    injetion_setting41 = models.CharField(max_length=20) # 퍼지 퍼지 설정(사출) - 압력 MPa
    injetion_setting42 = models.CharField(max_length=20) # 퍼지 퍼지 설정(사출) - 속도 %
    injetion_setting43 = models.CharField(max_length=20) # 퍼지 퍼지 설정(장전) - 압력 MPa
    injetion_setting44 = models.CharField(max_length=20) # 퍼지 퍼지 설정(장전) - 속도 %
    injetion_setting45 = models.CharField(max_length=20) # 퍼지 퍼지 설정(반복 횟수)
    injetion_setting46 = models.CharField(max_length=20) # 퍼지 퍼지 설정(장전 시간)
    injetion_setting47 = models.CharField(max_length=20) # 퍼지 퍼지 설정(장전 시간)

    message = models.TextField(null=True) # 메시지

    #/- 파일
    # file = models.FileField()

    #/- 오토 날짜
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name