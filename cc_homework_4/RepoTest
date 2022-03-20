class RepoTest {

    @Autowired
    private StudentRepository underTest;

    @Test
    void itSHouldCheckIfselectExistsEmail(){
        //given
        Person person = new person ("Rick", "Rick@gmail.com", Gender.FEMALE);
        underTest.save(student);
        //when
        boolean exists = underTest.selectExistsEmail(email);
        //then
        asserThat(exist).isTrue()
    }
}