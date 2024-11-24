# GYMVIM
헬스장 인원 파악 제휴 서비스
- 참여인원 : 6명
- 프로젝트 기간 : 2024-07 ~ 2024-08
- [GymBym 발표 ppt 보러가기](https://docs.google.com/presentation/d/117YGLrT9LOQEOik9-2FaK2x_qTCWJbkLZm0M9u5evkI/edit?usp=sharing)

## 목차
* [서비스 소개](#서비스-소개)
* [기술 스택](#백엔드-기술-스택)
* [소프트웨어 아키텍처](#소프트웨어-아키텍처)


## 서비스 소개<a id="서비스-소개"></a>
### 개발 필요성
<p>헬스를 하다보면 내가 사용하고 싶은 운동기구를 다른 사람이 사용하고 있을 때가 참 많습니다. 특히 사람이 많은 헬스장이거나 많이 몰리는 시간대이면 그날 하루는 그 운동을 못하는 상황이 발생하게 됩니다. 이럴 때 운동 기구 사용 현황을 제공해주는 사이트가 있다면 현재 운동 기구가 사용되고 있는 지 확인하고 사용 가능한 시간에 맞춰가면 되기 때문에 위 같은 문제가 해결될 것입니다.</p>

### 문제 솔루션
운동기구 사용량을 실시간으로 측정하여 현재 운동 기구마다 사용 현황 정보를 제공해 줄 수 있습니다.

### 타깃 고객층
헬스장 사장님 : 
- 회원이 너무 많아 운동 기구 사용에 불편을 겪고 있으며 고객의 불편을 해소시키기 위해서 헬스장 확장을 염두해 두고 계시는 사장님
- 새롭게 헬스장을 창업&분점을 내려고 하는 데 이러한 문제를 미리 방지하고 싶으신 사장님.

### 핵심 기능
| 기능                           | 설명                                                                                             |
|-------------------------------|--------------------------------------------------------------------------------------------------|
| 헬스장 입&퇴실                 | 헬스장 입실할 때와 퇴실할 때 태그를 찍으면 기록을 남깁니다.                                           |
| 로그인                        | 사용자의 개인정보를 받습니다.                                                                       |
| 회원 목록 관리                 | pt 트레이너는 회원 검색 시 특정 회원을 찾을 수 있고, 개인 정보(현재 운동량)을 확인할 수 있습니다.       |
| 회원 일정 관리                 | pt 트레이너는 회원의 운동 일정을 추가하거나 삭제할 수 있으며, 이는 회원 일정에도 반영됩니다.            |
| rfid 정상 작동                | RFID 태그가 정상 작동하는 지 확인합니다.                                                            |
| NFC 수정                      | 데이터베이스에 저장된 NFC 고유 id값을 수정합니다.                                                    |
| web에서 운동기구 예약          | 홈페이지에서 운동기구를 예약할 수 있습니다.                                                          |
| 태그 찍고 운동기구 사용         | 운동기구 옆에 붙어있는 단말기에 자신의 key를 가져다 대면 운동기구 사용중으로 데이터베이스에 저장됩니다.  |
| 예약된 운동기구를 사용으로 전환 | 예약된 시간이 되면 예약 -> 사용중으로 전환됩니다.                                                    |

### 왜 Raspbarry pi를 사용했을까?
[Raspbarry pi를 사용한 이유](https://www.notion.so/likelion/Raspberry-Pi-ff20056a10ed433b8af565bd3bf79e7e)

## 기술 스택<a id="백엔드-기술-스택"></a>
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-C51A4A?style=for-the-badge&logo=raspberry-pi&logoColor=white)
![RPi.GPIO](https://img.shields.io/badge/RPi.GPIO-0078D7?style=for-the-badge&logo=python&logoColor=white)
![MFRC522](https://img.shields.io/badge/MFRC522-009688?style=for-the-badge&logo=nfc&logoColor=white)

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)

<!-- - **Raspberry Pi**: 저렴하고 강력한 싱글 보드 컴퓨터
- **RPi.GPIO**: Raspberry Pi의 GPIO 핀을 쉽게 제어할 수 있게 해주는 라이브러리
- **MFRC522**: RFID/NFC 리더 모듈을 다루기 위한 라이브러리로, 카드 인식 및 데이터 전송 기능을 제공 -->

## 소프트웨어 아키텍처<a id="소프트웨어-아키텍처"></a>
### ERD 설계도
![erd image](./static/gym_vym%20ERD.png)


