<h2 align="center"><b><span style="font-size: larger;">Recommended Topic Hashtags</span></b></h2>
  
<p align="center">
  <img src="https://github.com/CapHaTri/Recommend-Topic-Hashtags/assets/113035712/caedaa42-319d-46a7-aff8-643d53332bd0" alt="Description of image">
</p>


# Mô tả bài toán

* **Ngữ cảnh ứng dụng**:
  * Trong các nhóm facebook, hashtag được sử dụng rộng rãi để gắn thẻ và tổ chức các bài viết. Tuy nhiên, việc tìm kiếm và sử dụng hashtag phù hợp lại khá thụ động và tốn nhiều thời gian cho người dùng. Và còn tồn tại rất nhiều bài viết trong group chưa được gán hashtag. Do đó, việc xây dựng một hệ thống có thể tự động đề xuất các hashtag liên quan cho nội dung bài viết trong các nhóm Facebook là khá quan trọng
  * Giới hạn nội dung là các bài post trong group facebook có liên quan đến lĩnh vực Computer Science
* **INPUT và OUTPUT Bài toán:**
  * INPUT: 
    * Nội dung một bài post : chỉ bao gồm dữ liệu dạng văn bản
    * Bộ dữ liệu đào tạo bao gồm text và các nhãn (hashtags) tương ứng
  * OUTPUT: 
    * Đưa ra gợi ý hashtags (có trong tập dữ liệu)

# Xây Dựng Bộ Dữ Liệu
* **Việc thu thập dữ liệu:**
  * Crawl dữ liệu trên 2 group: [Forum Machine Learning cơ bản](https://www.facebook.com/groups/machinelearningcoban) và [Group hỏi đáp Python, Data Science, Machine Learning, Deep Learning](https://www.facebook.com/groups/dsmlvietnam) 
* **Gán nhãn bộ dữ liệu**
  * Quy trình gán nhãn bộ dữ liệu
      <img src="https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/2ce8b609-2f3f-494d-ab9b-18701655cc08"/>
      <div style=width: 130px; align = center>Quy trình gán nhãn dữ liệu</div>
  * Hướng dẫn gán nhãn dữ liệu
      * Đĩnh nghĩa các nhãn dữ liệu
        * #sharing : có nội dung chia sẻ kinh nghiệm, job, tài liệu, cuộc thi, webinar,..
        * #machine_learning: có nội dung về các bài toán, thuật toán Machine Learning truyền thống như:  Linear Regression, Logistic Regression, scalar,... hoặc liên quan về road_map,..
        * #deep_learning: có nội dung về các bài toán, thuật toán Deep Learning hiện đại như: LSTM, Transformer,..  hoặc liên quan về road map,..
        * #python : có nội dung liên quan về code python, hoặc các thư viện hỗ trợ như  pytorch, tensorflow, pandas… 
        * #data: có nội dung liên quan đến dữ liệu , xử lý dữ liệu ,.., hoặc liên quan về road map, nghề nghiệp về data
        * #cv: có nội dung liên quan đến bài toán thuộc lĩnh vực Computer Vision, hoặc liên quan về road map, nghề nghiệp trong lĩnh vưc Computer Vision,.
        * #nlp: có nội dung liên quan đến bài toán thuộc lĩnh việc NLP, hoặc liên quan về road map, nghề nhiệp trong lĩnh vực NLP,..
        * #math: có nội dung liên quan đến kiến thức toán học như xác suất thống kê, đại số, giải tích,..
        * #Q&A: có nội dung liên quan đến hỏi đáp về một số vấn đề trong lĩnh vực Computer Science
* **Các bước tiền xử lý dữ liệu**
    * Normalize: xóa ký tự xuống dòng, lowercase toàn bộ văn bản.
    * Remove hastags, links, emojis: xóa những hashtags (chuỗi bắt đầu bằng '#'), những links (chuỗi bắt đầu bằng 'http') và các emoji.
    * Tokenizer: dùng pyvi.ViTokenizer.
        * Ví dụ:  công cụ ai giúp tăng tốc độ học của bạn link to pdf ->  công_cụ ai giúp tăng_tốc_độ học của bạn link to pdf
    * Encode number: chuyển các số trong văn bản thành '<number>'.
    * Delete one-length token: xóa những token có độ dài bằng 1.
  <div align="middle"> <img src="https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/3c299271-c480-4f48-a8be-1d9ab23ab5b8"/> </div>
  <div style=width: 130px; align = center>Các bước tiền xử lý dữ liệu</div>
* **Phân chia dữ liệu train-test**
    * Các bước chia dữ liệu
      * Với mỗi hashtag, lấy 10% data để tạo tập test.
      * Xóa những samples trùng nhau ở tập test.
      * Loại bỏ samples trong tập test ở data gốc để tạo tập train.
    <div align="middle"> <img src="https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/7c839333-fece-4466-9e4e-d3ca80ab970f"/> </div>
    <div style=width: 130px; align = center>Minh họa cách phân chia dữ liệu</div>
    * Kết quả sau khi phân chia dữ liệu
      <div align="middle"> <img src="https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/4585e789-184d-47bc-ac13-7ff18643a53c"/> </div>
* **Tổng quan về Bộ Dữ liệu:**
  *  Bộ dữ liệu: gồm 1282 mẫu dữ liệu  
  * Thống kê dữ liệu sau khi gán nhãn
    
      <div align="middle"> <img src="https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/4fc24414-80f3-44ff-ad32-d3f8bda3af85"/> </div>  
      <div style=width: 130px; align = center>Thống kê dữ liệu sau khi gán nhãn</div>
  * Thống kê về độ dài của các câu trong tập dữ liệu
      <div align="middle"> <img src= "https://github.com/Khanh-21522203/CS114.O11.KHCL-21522203/assets/117832185/c9fe4358-acd0-4f3f-bb3a-d935aa070d8f"/> </div>  
      <div style=width: 130px; align = center>Thống kê về độ dài của các câu</div>
      
# Training Và Đánh Giá Model
  * Phương pháp sử dụng
    * TF-IDF, BOW với mô hình Logistic Regression, SVM, Naive Bayes
  * Evaluation
    * Accuracy
      
      ![image](https://github.com/CapHaTri/Recommend-Topic-Hashtags/assets/113035712/ec925614-6f79-433a-804d-b063a802f7bd)
      
    * Precision
      
      ![image](https://github.com/CapHaTri/Recommend-Topic-Hashtags/assets/113035712/6fff23f1-c8c6-45a1-95f9-28d7ee5e8e52)
      
    * Recall
      
      ![image](https://github.com/CapHaTri/Recommend-Topic-Hashtags/assets/113035712/11a9466a-2438-4ec5-b1c1-80d8c818f343)
      
    * F1-Score
      
      ![image](https://github.com/CapHaTri/Recommend-Topic-Hashtags/assets/113035712/82956a6b-70a7-469a-b01c-00a2a7563624)

  * Result

  ![image](https://github.com/CapHaTri/Recommend-Topic-Hashtags/assets/113035712/4210624e-c767-4e72-81d7-98a94a9e76b6)

  ![image](https://github.com/CapHaTri/Recommend-Topic-Hashtags/assets/113035712/06dab66e-a5a0-4f14-9414-64f3af1e8f8c)

  ![image](https://github.com/CapHaTri/Recommend-Topic-Hashtags/assets/113035712/ed65e50d-6093-4afa-8acc-5de13c811c52)

# Demo 
* Sử dụng Streamlit để demo sản phẩm

![image](https://github.com/CapHaTri/Recommend-Topic-Hashtags/assets/113035712/448edbc7-aefa-44cd-8724-b00a4743a60e)
