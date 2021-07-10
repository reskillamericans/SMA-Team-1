const array = [{
    email: 'usman@gmail.com',
    password: '123'
 }, {
    email: 'ali@gmail.com',
    password: '123'
 }];

 
 const matchCredentials = (email, password) => {
    const match = array.find(el => {
       return el.email === email && el.password === password;
    });
    return !!match;
 };
 console.log(matchCredentials('usman@gmail.com', '123'));
 console.log(matchCredentials('usman@gmail.com', '1423'));