import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Header } from './Components/Header/header';
import { Footer } from './Components/Footer/footer';
import {
  ErrorPage,
  StartPage,
  LoginPage,
  RegistrationPage,
  ListingPage,
  HelperListPage,
  JobListPage,
  HelperProfilePage,
  HelperInfo,
  HelperJobs,
  SearchPage,
  AboutPage,
  MyProfilePage,
  NewJob,
  Job,
  MapPage,
  ViewJob,
  PrivateJob,
  RegisterHomepage,
  RegisterHelper,
  RegisterMember,
  MenuBar,
} from './Pages';

export const RoutesIndex = () => {
  return (
    <>
      <BrowserRouter>
        <Header />
        <main className="p-5">
          <Routes>
            <Route path="/" element={<StartPage />} />
            <Route path="registration" element={<RegistrationPage />} />
            <Route path="login" element={<LoginPage />} />
            <Route path="search" element={<SearchPage />} />
            <Route path="menu" element={<MenuBar />} />
            <Route path="new-job" element={<NewJob />} />
            <Route path="view-job" element={<ViewJob />} />

            <Route path="register" element={<RegisterHomepage />} />
            <Route path="member-register" element={<RegisterMember />} />
            <Route path="helper-register" element={<RegisterHelper />} />

            <Route path="listing" element={<ListingPage />}>
              <Route index element={<HelperListPage />} />
              <Route path="helpers" element={<HelperListPage />} />
              <Route path="jobs" element={<JobListPage />} />
            </Route>

            <Route path="Job" element={<Job />} />

            <Route path="helper-profile" element={<HelperProfilePage />}>
              <Route index element={<HelperInfo />} />
              <Route path="info" element={<HelperInfo />} />
              <Route path="jobs" element={<HelperJobs />} />
            </Route>

            <Route path="private-job" element={<PrivateJob />} />
            <Route path="my-profile" element={<MyProfilePage />} />

            <Route path="maps" element={<MapPage />} />

            <Route path="about" element={<AboutPage />} />
            <Route path="*" element={<ErrorPage />} />
          </Routes>
        </main>
        <Footer className="p-5" />
      </BrowserRouter>
    </>
  );
};
