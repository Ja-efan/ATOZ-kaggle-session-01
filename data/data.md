# Bank Customer Churn Prediction 
---

## About Dataset 
---
은행 고객 이탈 데이터 셋은 은행(금융) 산업에서 고객 이탈을 예측하는 데 많이 사용 된다.  
해당 데이터 셋은 은행을 떠난, 즉 해당 은행에서 탈퇴한 고객 정보와 여전히 가입을 유지하는 고객 정보를 모두 담고 있다.  
데이터 셋에 포함된 특성(attribute)은 다음과 같다.

1. **Customer ID**  (numeric)  
  고객의 고유 ID

    - 중복이 존재함 (Distinct 14.1%)

2. **Surname**  (*object*)  
  고객의 이름(성)

3. **CreditScore**  (numeric)  
  고객 신용 점수  
  
4. **Geography**  (*object*)  
  고객 거주 국가

5. **Gender**  (*object*)  
  고객 성별 

6. **Age**  (numeric)  
  고객 나이 

7. **Tenure**  (numeric)  
  가입 기간

8. **Balance**  (numeric)  
  통장 잔고   

9. **NumOfProducts**  (numeric)  
  가입 상품 개수 

10. **HasCrCard**  (numeric)  
  신용 카드 보유 여부 

11. **IsActiveMember**  (numeric)  
  고객 활동 여부 (휴면 고객 여부?)

12. **EstimatedSalary**  (numeric)  
  고객 예측 연봉   

13. **Exited**  (numeric: target)  
  고객 이탈 여부   
