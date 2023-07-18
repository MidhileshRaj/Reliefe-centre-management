function select()
{
    var a = document.getElementById('state').value;
    if(a==="Kerala")
    {
        var array=["Kasaragod","Kannur","Wayanad","Kozhikode","Malappuram","Palakkad","Thrissur","Eranakulam","Idukki","Kottayam","Alappuzha","Pathanamthitta","Kollam","Thiruvananthapuram"];
    }
    else if(a==="Tamilnadu")
    {
        var array=["Kanchipuram","Tiruvallur","Cuddalore","Villupuram","Vellore","Tiruvannamalai","Salem","Namakkal","Dharmapuri","Erode","Coimbatore","The Nilgiris","Thanjavur",
        "Nagapattinam","Tiruvarur","Tiruchirappalli","Karur","Perambalur","Pudukkottai","Madurai","Theni","Dindigul","Ramanathapuram","Virudhunagar","Sivagangai","Tirunelveli","Thoothukkudi",
        "Kanniyakumari","Krishnagiri","Ariyalur","Tiruppur"];
    }
    else if(a==="Karnatka")
    {
         var array=["Bagalkot","Bengaluru Urban","Bengaluru Rural","Belagavi","Ballari","Bidar","Vijayapur","Chamarajanagar","Chikballapur","Chikkamagaluru","Chitradurga","Dakshina Kannada","Davanagere",
         "Dharwad","Gadag","Kalaburagi","Hassan","Haveri","Kodagu","Kolar","Koppal","Mandya","Mysuru","Raichur","Ramanagara","Shivamogga","Tumakuru","Udupi","Uttara Kannada","Yadgir"];
    }
    else if(a==="Goa")
    {
        var array=["North Goa","South Goa"];
    }

    var string="";
    for (i = 0 ; i<array.length ; i++)
    {
        string=string+"<option>"+array[i]+"</option>";
    }
    string="<select name='district' required>"+string+"<option selected>Select district</option></select>";
    document.getElementById('district').innerHTML=string; 
}