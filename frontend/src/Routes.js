import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Header } from './Components/Header/header';
import { Footer } from './Components/Footer/footer';
import {
  ErrorPage,
  HomePage,
  LoginPage,
  RegistrationPage,
  ListingPage,
  ProfilePage,
  SearchPage,
} from './Pages';

export const RoutesIndex = () => {
  return (
    <>
      <BrowserRouter>
        <Header />
        <main className="p-5">
          <Routes>
            <Route index element={<HomePage />} />
            <Route path="/" element={<HomePage />} />
            <Route path="registration" element={<RegistrationPage />} />
            <Route path="profile" element={<ProfilePage />} />
            <Route path="login" element={<LoginPage />} />
            <Route path="search" element={<SearchPage />} />
            <Route path="listing" element={<ListingPage />} />
            <Route path="*" element={<ErrorPage />} />
          </Routes>
        </main>
        <Footer className="p-5" />
        {/* <Route path="search" element={<Search />}>
              <Route index element={<Restaurants />} />
              <Route path="restaurants" element={<Restaurants />} />
              <Route path="reviews" element={<SearchReviews />} />
              <Route path="users" element={<Users />} />
            </Route>
            <Route path="restaurant">
              <Route path=":restaurantID" element={<RestaurantPage />} />
            </Route>
            <Route path="reviews/new" element={<NewReview />} />
            <Route path="profile" element={<Profile />}>
              <Route index element={<Reviews />} />
              <Route path="reviews" element={<Reviews />} />
              <Route path="comments" element={<Comments />} />
              <Route
                path="my-restaurants"
                element={<ProfileRestaurants />}
              ></Route>
              <Route path="edit-profile" element={<EditProfile />} />
            </Route>
            <Route path="restaurants/new" element={<NewRestaurant />} />

            <Route path="register" element={<Register />}>
              <Route index element={<RegistrationForm />} />
              <Route path="success" element={<RegisterSuccessPage />} />
              <Route path="new_user" element={<NewUserForm />} />
              <Route path="*" element={<ErrorPage />} />
            </Route> */}
      </BrowserRouter>
    </>
  );
};